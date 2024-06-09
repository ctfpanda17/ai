import gymnasium as gym
import time

env = gym.make("CartPole-v1", render_mode="human") # 若改用這個，會畫圖
# env = gym.make("CartPole-v1", render_mode="rgb_array")
observation, info = env.reset(seed=42)
def choose_action(observation):
    pos, v, ang, rot = observation # 車位置、車速度、柱角度、柱角速度
    
    weighted_sum = 1.0 * ang + 0.5 * rot
    # 根據加權值的正負選擇動作
    return 0 if weighted_sum < 0 else 1

    # 角度 < 0 選擇 action 0（車向左），否則選擇 action 0（車向右）
    #return 0 if ang < 0 else 1

score = 0 
for _ in range(1000):
   start = time.time()
   env.render()
   action = choose_action(observation)  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)
   score += reward
   if terminated or truncated:   
      observation, info = env.reset()
      print('done ,score=', score)
      score = 0
      
env.close()