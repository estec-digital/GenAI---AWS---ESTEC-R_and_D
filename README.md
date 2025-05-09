# GenAI---AWS---ESTEC-R_and_D
This repository will guide gradually setting up geniel in the AWS environment ☁️
# Section 1: Start setup 🚀
## Step 1.1: Create Agent 🤖
- Click "**Create agent**" button at the right corner
    ![alt text](image.png)
- Enter the name for **Agent Name** field
  - **Example**: AgentAI-Estec
- Enter the description for **Agent Description** field
  - **Example**: Estec Agent AI hỗ trợ truy vấn cơ sở dữ liệu DCS của nhà máy xi măng Bình Phước.
    ![alt text](image-1.png)
- Choose option "**Use an existing service role**"
    ![alt text](image-2.png)
- Select model for agent
    ![alt text](image-4.png)
- Enter the instructions for "**Instructions for the Agent"** field
  - **Example**: Bạn là một trợ lý ảo. Hãy thêm phần responses vào cuối mỗi câu. Khi người dùng hỏi về giá trị cảm biến tại thời điểm nào đó bạn nên dùng action_group_truy_van_gia_tri_cam_bien theo tên cảm biến và thời gian truy vấn và trả về giá trị tương ứng 
    ![alt text](image-5.png)
- Click "**Save**" button to save setting
    ![alt text](image-6.png)
## Step 1.2: Create Action Group