import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1=nn.Linear(input_size, hidden_size)
        self.linear2=nn.Linear(hidden_size, output_size)


    def forward(self, x):
        x=F.relu(self.linear1(x))
        x=self.linear2(x)
        return x
    
    def save(self, file_name='model.pth'):
        model_folder_path='./model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
            
        file_name=os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)


class QTrainer:
    def __init__(self, model, lr, gamma):
        self.lr=lr
        self.gamma=gamma
        self.model=model

        self.criterion=nn.MSELoss()
        self.optimizer=optim.Adam(model.parameters(),lr=self.lr)


    def train_step(self, state, action, reward, next_state, done):
        state=torch.tensor(state, dtype=torch.float)
        action=torch.tensor(action, dtype=torch.float)
        reward=torch.tensor(reward, dtype=torch.float)
        next_state=torch.tensor(next_state, dtype=torch.float)
     
        if len(state.shape)==1:
            #means only 1 dim but we want it in dim (1,x), 1=no. of batches. i.e to simulate batch of size 1
            state=torch.unsqueeze(state,0)
            action=torch.unsqueeze(action,0)
            reward=torch.unsqueeze(reward,0)
            next_state=torch.unsqueeze(next_state,0)
            done=(done,)

        #1:predicted q values withcurrent state
        pred=self.model(state) #shape=[batch_size,num_actions=3],these are the estimated q_values given by model
        target=pred.clone()
        for idx in range(len(done)): #len(done)=len(state)=len(action)......=batch_size
            Q_new=reward[idx]
            if not done[idx]:
                Q_new=reward[idx]+self.gamma*torch.max(self.model(next_state[idx])) #bellman equation
                #self.model(next_state[idx]) gives 3 outputs, i.e 3 Q-values for 3 actions possible in next state
        target[idx][torch.argmax(action).item()]=Q_new #updates Q_values given by the model
        self.optimizer.zero_grad()
        loss=self.criterion(pred, target)
        loss.backward()
        self.optimizer.step()

             

