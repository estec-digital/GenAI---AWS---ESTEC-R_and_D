# Add Lambda policy to allow Amazon Bedrock access to invoke the Lambda function. ( Thêm chính sách của Lambda cho phép Amazon Bedrock truy cập gọi hàm Lambda ) 

- **Click** **Configuration** - **Permissions** - **Add** **permissions**
![[image26.png]]
- Choose the **AWS Service**
	- Choose the **Other option**
![[image27.png]]
- **Enter** the **Statement ID**
	- **Example** : allowBedrockInvoke
- **Enter** the **Principal**
	- **Example** : bedrock.amazonaws.com
- **Enter** the **Source** **ARN**
> [!info]
> - Example : You can get the Source ARN of Bedrock in this 
> - ![[image29.png]]
- **Enter** the **Action**
	- **Example** : lambda: InvokeFunction
- **Click Save**
![[image28.png]]
---
# Add Lambda policy to allow DynamoDB access to invoke the Lambda function. ( Thêm chính sách của Lambda cho phép DynamoDB truy cập gọi hàm Lambda ) 

- Click Add permissions
![[image30.png]]
- Choose the **AWS Service**
	- Choose the **Other option**
- **Enter** the **Statement ID**
	- **Example** : DynamodbAccess
- **Enter** the **Principal**
	- **Example** : bedrock.amazonaws.com
- **Enter** the **Source** **ARN**
> [!info]
> **Example** : You can get the Source ARN of DynamoDB in this  
> 	 ![[image32.png]]

![[image31.png]]**Click Save** after **enter all the information**.