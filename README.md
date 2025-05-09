# GenAI---AWS---ESTEC-R_and_D
This repository will guide gradually setting up geniel in the AWS environment ☁️
# Section 1: Start setup 🚀
## Step 1.1: Create Agent 🤖
- Click "**Create agent**" button at the right corner

![alt text](Photos/image.png)
- Enter the name for **Agent Name** field
- **Example**: AgentAI-Estec
- Enter the description for **Agent Description** field
- **Example**: Estec Agent AI hỗ trợ truy vấn cơ sở dữ liệu DCS của nhà máy xi măng Bình Phước

![alt text](Photos/image-1.png)
- Choose option "**Use an existing service role**"

![alt text](Photos/image-2.png)
- Select model for agent

![alt text](Photos/image-4.png)
- Enter the instructions for "**Instructions for the Agent"** field
- **Example**: Bạn là một trợ lý ảo. Hãy thêm phần responses vào cuối mỗi câu. Khi người dùng hỏi về giá trị cảm biến tại thời điểm nào đó bạn nên dùng action_group_truy_van_gia_tri_cam_bien theo tên cảm biến và thời gian truy vấn và trả về giá trị tương ứng.

![alt text](Photos/image-5.png)
- Click "**Save**" button to save setting

![alt text](Photos/image-6.png)
---
## Step 1.2: Create Lambda Function 🔺
- Click "**Create function**" button to create Lambda Function

![alt text](Photos/image12.png)
- Choose **Author from scratch**
- Enter function name for **Function name** field
- Choose language for lambda function
- Choose **x86_64** option
- Click "**Create function**" button at right footer corner to complete create new lambda function


![alt text](Photos/image11.png)

![alt text](Photos/image13.png)
---
## Step 1.3: Create Action Group 🤝
- Click "**Add**" button to create Action Group
  
![alt text](Photos/image7.png)
- Enter the **Action group name** field
  - **Example**: action_group_estec_genai
- Enter the **Description** field
  - **Example**: Action group này dùng để truy xuất thông tin người dùng từ bảng DynamoDB được cung cấp. Agent sẽ gọi Lambda function để truy vấn dữ liệu từ DynamoDB và trả về kết quả phù hợp.

![alt text](Photos/image8.png)
- Choose **Define with API schemas** option

![alt text](Photos/image9.png)
- Choose **Select an existing Lambda function** option in **Action group invocation**

![alt text](Photos/image10.png)