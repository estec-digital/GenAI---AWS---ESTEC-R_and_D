---
aliases:
  - ESTEC - AWS Gen AI Workshop
sticker: emoji//1f61d
banner: projects/estec-machine-learning-frontend/src/assets/images/logo.png
---
****# ESTEC - AWS Gen AI Workshop

```table-of-contents
```
---
# **Introduction**

# Bedrock Agents Chatbot - Recommend & Order

## Overview

This is a fullstack Chatbot app that is able to help a customer find a new drink based on preferences such as calories, allergens, flavors, or seasonal trends. After a drink is found it will walk the customer through the order process and submit the order. The Chatbot is able to surface recommendations via Bedrock Knowledge base using product data stored in S3. The Chatbot is **also** able to access known customer preferences from Datastore, find local store locations for pickup, and submit order to Commerce engine using Bedrock Agents. This is 100% Serverless and is well architected. Demo -> POC in a matter of hours!

![image](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/ui.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzA5ODYxOH19fV19&Signature=ArfC2nN-aKUqRaBO5pln9x23qRBhkYdeoNMMbwM5mZ8YKq%7EpsWotCirljOajNltmvafHzQygmrqSEAuF8yaf16%7E5T6fzlOmJnUbjYHrQtOH00nCV41DjYJT6sfkSkAvy-ANOsZ8b9SO1UKx6Mf4TmhfNwMxHfpVzby5ZpaxYLHBRcHAcyfGrm4uRva0VdXNlVJefWKmR-ioCXZRTKeWI3t6YoZFj2khnB62lRDQJxoQ3l8F3rO2N2jpLuGC8Zrtqd2j0v6XwtOS9OeeE4k2KgHA9CVMjQuKCszo8gIZZnPUIkznLrh1926gWvz7CTx1GlQaXpT9fNEzzt1A2wsSRUg__)

This is a fullstack Chatbot app that is able to help a customer find a new drink based on preferences such as calories, allergens, flavors, or seasonal trends. After a drink is found it will walk the customer through the order process and submit the order. The Chatbot is able to surface recommendations via Bedrock Knowledge base using product data stored in S3. The Chatbot is also able to access known customer preferences from Datastore, find local store locations for pickup, and submit order to Commerce engine using Bedrock Agents. This is 100% Serverless and is well architected.
## FEATURES

- Simple React Frontend Template (Easily Configurable to meet customer brand image)
- Bedrock Agents integration (Lambda Actions Code)
- OpenAPI Pattern Example
- Vector DB via Knowledge Base (Just upload example file to S3 and sync)
- Secured Frontend and APIGateway via Cognito / JWT
- DynamoDB tables for Customers, Orders, and Locations (Accessed by Agent)

![image](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/architecture.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzA5ODYxOH19fV19&Signature=ArfC2nN-aKUqRaBO5pln9x23qRBhkYdeoNMMbwM5mZ8YKq%7EpsWotCirljOajNltmvafHzQygmrqSEAuF8yaf16%7E5T6fzlOmJnUbjYHrQtOH00nCV41DjYJT6sfkSkAvy-ANOsZ8b9SO1UKx6Mf4TmhfNwMxHfpVzby5ZpaxYLHBRcHAcyfGrm4uRva0VdXNlVJefWKmR-ioCXZRTKeWI3t6YoZFj2khnB62lRDQJxoQ3l8F3rO2N2jpLuGC8Zrtqd2j0v6XwtOS9OeeE4k2KgHA9CVMjQuKCszo8gIZZnPUIkznLrh1926gWvz7CTx1GlQaXpT9fNEzzt1A2wsSRUg__)

---
# Module 1 - Configure the Environment

## I. Getting Started with AWS CloudShell or Your Own Workstation

### Using AWS CloudShell

This workshop can be completed using [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html)  from the AWS Management Console.

AWS CloudShell is a browser-based, pre-authenticated shell that you can launch directly from the AWS Management Console. When you launch AWS CloudShell, a [compute environment](https://docs.aws.amazon.com/cloudshell/latest/userguide/vm-specs.html#vm-configuration)  that's based on Amazon Linux 2023 is created. Within this environment, you can access an [extensive range of pre-installed development tools](https://docs.aws.amazon.com/cloudshell/latest/userguide/vm-specs.html#pre-installed-software) , options for uploading and downloading files, and file storage that persists between sessions.

Simply start AWS CloudShell by clicking on the console icon near the top, right side of the console screen. ![AWS CloudShell](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/start_cloudshell.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)


### Using Your Own Workstation

You can also accomplish this workshop on your own system. Make sure your evnironment meets the following requirements.

**Requirements**

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html)  if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)  installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)  (AWS SAM) installed
- [Node 18x](https://nodejs.org/en/blog/release/v18.18.1)  for Frontend React Build

If you are using your own evnironment, you will need to import the workshop's participant credentials. If you are using AWS CloudShell, you do not need to do this.

1. Get your AWS CLI Credentials from workshop studio side bar. Copy the credentials for **Linux or macOS (bash)**.
    
    ![AWS Creds](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/aws_creds.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)
    
2. Paste them into your terminal and hit enter.
    
    ![Copy Creds](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/copy_creds.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

## II. Deploy Cloudformation Stack
### 1.1 Download the Cloudformation Code from the Workshop

1. In the terminal, download the Cloudformation Code.

```bash
curl 'https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/code.zip?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys~BzR780hO22lfP2w13zccWOxIfDKYKH5FM~z9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL~J4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__' --output code.zip
```

3. Unzip code.zip and enter code directory

```bash
unzip code.zip
```

```bash
cd bedrock-agents-order-bot-workshop
```

### 1.2 Build and Deploy Cloudformation

1. From the command line, change director to ./backend directory and use AWS SAM to deploy the AWS resources for the backend as specified in the template.yaml file:

```bash
cd backend
```

```bash
sam build && sam deploy --guided
```

2. During the prompts:
    
    - Enter a stack name: `digital-barista`
    - Enter the desired AWS Region: `us-west-2`

> [!important]
> You will need to enter an email address that you have access to. This will be used to access the front end later on in the lab!

    
    - Enter Email for Cognito user creation (_Check email for password after_)
    - Allow SAM CLI to create IAM roles with the required permissions
    - Keep everything else as Default

> [!info]
> The deployment can take up to 15 mins because of the setup needed for Cloudfront


---
# Module 2 - Set up Knowledge Base and Agents
## I. Set up S3 with Product Data

Knowledge bases for Amazon Bedrock provides you the capability of amassing data sources into a repository of information. With knowledge bases, you can easily build an application that takes advantage of retrieval augmented generation (RAG), a technique in which the retrieval of information from data sources augments the generation of model responses.

Now that you have configured your enviornment, it's time to setup a data source source for your knowledge base. A data source contains files with information that can be retrieved when your knowledge base is queried. You set up the data source for your knowledge base by uploading source document files to an Amazon S3 bucket.

For this step, you will download a zip that contains the product information in PDF format. You will copy the PDFs to an S3 bucket that was created during the Cloudformation deployment process. The knowledge base will use this S3 bucket as its data source.

1. In the terminal, change directory to the home folder.

```bash
cd ~
```

2. From the CLI, run the following command to list the S3 buckets in your account.

```bash
aws s3 ls
```

![s3 ls results](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/s3_ls_results.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

Several S3 buckets may be listed. Take note of the S3 bucket that is named `digital-barista-bedrockknolwedgebasebucket-{RandomString}`. Copy this name. This will be the destination S3 bucket that you will upload the product data to.

3. Now, download the **product-data** zip. This zip contains the drink data in CSV format that will be the source data for the knoweldge base.

```bash
curl 'https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/assets/product-data.zip?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys~BzR780hO22lfP2w13zccWOxIfDKYKH5FM~z9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL~J4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__' --output product-data.zip
```

4. Unzip product-data.zip and change directory to **product-data** directory

```bash
unzip product-data.zip
```

```bash
cd product-data
```

> [!important]
> 
> Make sure you are in the **product-data** directory before the next step.


4. Now copy the data from **product-data** to the S3 bucket. Copy the command below and modify it to reflect your S3 bucket for the workshop.

```bash
1
aws s3 cp . s3://digital-barista-bedrockknowledgebasebucket-{RandomString}/ --recursive
```

1. To confirm the copy was successful, navigate to **Amazon S3** in the **AWS console**. You may need to click **Buckets** on the left hand menu if there isn't a list of S3 buckets. Click on your `digital-barista-bedrockknolwedgebasebucket-{RandomString}` bucket to see its contents. There are 8 product category CSVs that should have been copied. ![bucket domain data](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/bucket_domain_data.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

## II. Grant Model Access

1. Before we setup the knowledge base, we will need to grant access to the large language models that RAG and the agent will use. Access to Amazon Bedrock foundation models isn't granted by default. Navigate to **Amazon Bedrock** from the **AWS console**. On the left of the screen, scroll down and select **Model access**. On the top center, select the **Enable specific model** button.

![Model access](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/model_access.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

2. Select the checkbox for the base model columns **Titan Text Embeddings V2** and **Anthropic: Claude Haiku & Sonnet**. This will provide you access to the required models. After, scroll down to the bottom right and select **Next**.

![Select models](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/select_models.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

3. Review model access modifications and then select **Submit** at the bottom right of the page.

![Submit access](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/submit_access.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

Attention: Gaining access to both models can take a few minutes.

4. After, verify that the access status of the models is green with **Access granted**.

![Access granted](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/access_granted.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

## III. Setup Knowledge Base

By this step, you have setup S3 and imported the product data. You have chosen your large language models and requested access to those models. Now you are ready to setup a knowledge base.

With Knowledge Bases for Amazon Bedrock, you can easily build an application that takes advantage of retrieval augmented generation (RAG), a technique in which the retrieval of information from data sources augments the generation of model responses. You can give FMs and agents contextual information from a company’s private data sources for RAG to deliver more relevant, accurate, and customized responses.

1. Navigate to the Amazon Bedrock console. On the left of the screen, scroll down and select **Knowledge base**. Then select the orange **Create knowledge base** button on the right side of the page.

![create_kb_btn](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/create_kb_btn.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

2. You can use the default name, or enter in your own. Leave all other settings default. Select **Next** at the bottom right of the screen to move forward.

![KB details](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/kb_details.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

3. In the middle, right side of the screen, select **Browse S3** and select the bubble for **digital-barista-bedrockknolwedgebasebucket-{RandomString}** S3 bucket. Once the bubble is selected and the S3 bucket is highlight, select **Choose** and proceed to the next page by selecting **Next** at the bottom.

![KB setup](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/KB_setup.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

4. For the embedding model, choose **Titan Text Embeddings V2**. Leave the other options as default, and scroll down to select **Next**.

![Vector Store Config](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/vector_store_config.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

5. On the next screen, review your work, then select **Create knowledge base**

Once your data source completes syncing you will be able to move to the next step. It can take about 5 mins to complete.

![Review and Create KB](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/review_create_kb.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

Important

Once you slect **Create Knowledge base**, AWS prepares the vector database in Amazon Opensearch Serverless. This process may take several minutes to complete. DO NOT navigate away from the page. Page will refresh once the deployment has completed.
## IV. Knowledge Base Data Sync

### Sync to ingest your data sources into the knowledge base

After you create your knowledge base, you ingest the data sources into the knowledge base so that they're indexed and able to be queried. Ingestion converts the raw data in your data source into vector embeddings. It also associates the raw text and any relevant metadata that you set up for filtering to augment the querying process.


> [!important]
> 
> You cannot continue with the sync until the Amazon Opensearch Serverless vector database deployment is complete!


If you did not navigate away from the Amazon Opensearch Serverless deployment, the page will automatically refresh stating the knowledge base is created successfully. Follow these next steps to now sync the data source with the knowledge base.

![knowledge base created](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/knowledge_base_created.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

1. On the **knowledge-base-quick-start** page, scroll down to **Data source**. Select the bubble for your **knowledge-base-quick-start-data-source** and select **sync**.

![data source sync](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/data_source_sync.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

2. At the top of the page, a blue bar will appear stating "**Sync started for data source**". Wiat for it to complete and then proceed to the next section of the workshop.

![sync inprogress](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/data_source_sync_inprogress.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

![sync complete](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/data_source_sync_complete.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

## V. Setup an Agent

### Agents for Amazon Bedrock

Agents for Amazon Bedrock offers you the ability to build and configure autonomous agents in your application. An agent helps your end-users complete actions based on organization data and user input. Agents orchestrate interactions between foundation models (FMs), data sources, software applications, and user conversations. In addition, agents automatically call APIs to take actions and invoke knowledge bases to supplement information for these actions. Developers can save weeks of development effort by integrating agents to accelerate the delivery of generative artificial intelligence (generative AI) applications .

With agents, you can automate tasks for your customers and answer questions for them. For example, you can create an agent that helps customers process insurance claims or an agent that helps customers make travel reservations. You don't have to provision capacity, manage infrastructure, or write custom code. Amazon Bedrock manages prompt engineering, memory, monitoring, encryption, user permissions, and API invocation.

In this workshop, your agent will be a digital barista that you will be able to interact with. Per the instructions that will be provided to the agent, it'll be able to provide drink information, drink recommendations and submit an order on your behalf.

1. To get started setting up your agent, navigate to the **Amazon Bedrock** in the AWS console. From the menu on the left hand side, select **Agents** under **Builder tools**. Then select **Create Agent**.

![bedrock agents](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/bedrock_agents.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

2. Provide an agent name, such as **DigitalBarista**, then select **Create**.

![create bedrock agent](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/create_bedrock_agent.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

3. Next, under **Select model**, leave **Anthropic as is but change the large language model to **Claude 3 Haiku**.
    
4. Next, provide the instructions for the agent. Copy the text below and paste it in the **Instructions for the Agent** prompt:
    

```instruction
You are an agent that helps customers purchase a drink. Retrieve customer details like customer ID, city, and likes based on the name. Provide first recommendation based on customer likes {likes}. Further recommendations are based on new customer preference prompt. Generate response with product name and calories. After customer indicates product they would like to order, use customer city {city} to get potential store locations. Confirm the store location. Confirm product name, product size, order total, and store location. Once confirmed, submit order with all required fields. On order success return confirmation message in format below. Your order {orderId} has been confirmed. Your drink will be ready in the next 5 mins at store {storeName}.
```

![agent config](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/agent_config.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

1. Select **Save** at the top of the screen and proceed to the next step of the workshop.
    
    
> [!important]
> You will lose **Instructions for the Agent** if you do not save and proceed to the next step!

> [!bug]
> Khi báo lỗi người dùng bị cấp quyền thiếu Policies khi tạo Agent thì ta fix bằng cách: 

![[image24.png]]

![[image25.png]]

> [!todo]
> Tạo Policies với tên SageMakerPublicHubAccess
> Chọn phần JSON
> Copy code phía dưới vào xong ấn Next

````
{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "sagemaker:ListHubContents", "Resource": "arn:aws:sagemaker:us-west-2:aws:hub/SageMakerPublicHub" } ] }
````

> [!todo]
> Tim WPParticipantRole trong Search IAM
> Sau đó phải attach file policies mới thêm vào


> ![[image23.png]]


> [!todo]
> Vào phần additional setting -> chọn enable all options

![[image22.png]]
## VI. Create an Action Group

### Create an action group for an Amazon Bedrock agent

An action group defines actions that the agent can help the user perform. For example, you could define an action group called BookHotel that helps users carry out actions that you can define such as:

In this step, you will create an action group by performing the following steps:

- Define the parameters and information that the agent must elicit from the user for each action in the action group to be carried out.
    
- Decide how the agent handles the parameters and information that it receives from the user and where it sends the information it elicits from the user.
    

For this workshop, these actions are already defined in a API schema provided in this section. You are importing it into the **Action group** as part of the creation process.

1. We will now create an **Action group**. Scroll past the **Agent Details** section where you added the **Instructions for the Agent**. The very next section is **Action groups**. Once there, then select **Add**.

![action group add](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/action_group_add.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

5. Name the action group **DigitalBarista-actions** and then for the **Action group type**, select **Define with API schemas**.

![action group details](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/action_groupw_details.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

6. Next, select the bubble for **Select an existing Lambda function**. Then, from the drop down menu for **Select Lambda function**, select `{StackName}-BedrockAgentsAction-{Random}`.

![action group invocation](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/action_groupw_invocation.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

7. For the **Action group schema**, select **Define via in-line schema editor**. Copy & paste the schema from below into the **In-line OpenAPI schema** editor in YAML.


> [!important]
> 
> Clear out any existing schema or make sure to copy and paste all the existing schema


This API schema is needed so that the bedrock agent knows the format structure and parameters required for the action group to interact with the Lambda function.

![action group schema](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/action_group_schema.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

```yaml
openapi: 3.0.0
info:
  title: Submit Order Automation API
  version: 1.0.0
  description: API for submitting orders and checking product inventory level
paths:
  /customer/{CustomerName}:
    get:
      summary: Get information about a customer
      description: Get information about a customer. Return customer details such as
        location city and likes.
      operationId: getCustomer
      parameters:
        - name: CustomerName
          in: path
          description: Customer Name
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Get Customer Information
          content:
            application/json:
              schema:
                type: object
                properties:
                  customerId:
                    type: string
                    description: The ID for the customer record
                  name:
                    type: string
                    description: Customers Name
                  city:
                    type: string
                    description: The city name the customer resides in
                  likes:
                    type: string
                    description: Preferences the customers enjoys in their drink
  /location:
    get:
      summary: Get store locations within a city
      description: Get store locations within a city. Returns pick-up stores for an order.
      operationId: getLocation
      parameters:
        - name: CityName
          in: query
          description: City name
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Get all stores that are in a city
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    locationId:
                      type: string
                      description: The ID for the store
                    storeName:
                      type: string
                      description: The name of the store
                    city:
                      type: string
                      description: The city for the store
                    address:
                      type: string
                      description: Address of store
                    hours:
                      type: string
                      description: store operating hours
  /submitOrder:
    post:
      summary: Submit order endpoint
      description: Submit customer order to the commerce endpoint. Return the order ID.
      operationId: submitCustomerOrder
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                customerName:
                  type: string
                  description: The customers name for the order
                productName:
                  type: string
                  description: Name or title of the product
                productSize:
                  type: string
                  description: The size of the product
                orderTotal:
                  type: string
                  description: Order total in US dollars
                storeName:
                  type: string
                  description: The store name for the pick-up location
              required:
                - customerName
                - productName
                - productSize
                - orderTotal
                - storeName
      responses:
        "200":
          description: Order submitted successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  orderId:
                    type: string
                    description: Unique Id to track the status of an order
        "400":
          description: Bad request. One or more required fields are missing or invalid

```

This API schema defines three primary endpoints, `/customer/{CustomerName}`, `/location`, and `/submitOrder` detailing how to interact with the API, the required parameters, and the expected responses.

8. Once you have pasted the schema, select **Create**. This will then take you back to the **Agent build: DigitalBarista** page. You should see your **DigitalBarista-actions** listed in the **Action groups**.

![action group complete](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/action_group_complete.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

## VII. Associate Knowledge Base with Agent

You can also associate the knowledge base with an agent and the agent will invoke it when necessary during orchestration.

1. On the **Agent builder: DigitalBarista** page, scroll past **Agent details** and **Action groups** till you get to the **Knowledge bases** section. Select **Add**

![agent add knowledge base](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/add_kb_to_agent.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

2. Choose the knowledge base from the dropdown list under **Select knowledge base** and specify the instructions for the agent regarding how it should interact with the knowledge base and return results.

A sample instruction has been provided below for you to copy and paste into the **Knowledge base instructions for Agent**

```text
1
Use this knowledge base to look up product and drink information.
```

![Knowledge base add2](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/add_kb.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

3. Review your input, then select **Add**. This will return you to the **Agent builder: DigitalBarista** page and you can now see your knowledge base has been added to the **Knowledge bases** section.

![Knowledge base complete](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/kb_complete.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

4. You are now finished configuring your agent. Scroll to the top of the page and select **Save** and then select **Prepare**. This will ensure your changes to the agent are saved and preparing the agent will allow it to be deployed. Once finshed, select **Save and exit**.

![save agent](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/save_agent.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

## VIII. Create Agent Alias

When you first create an Amazon Bedrock agent, you have a working draft version (DRAFT) and a test alias (TSTALIASID) that points to the working draft version. When you make changes to your agent, the changes apply to the working draft. You iterate on your working draft until you're satisfied with the behavior of your agent. Then, you can set up your agent for deployment and integration into your application by creating aliases of your agent.

To deploy your agent, you must create an alias. During alias creation, Amazon Bedrock creates a version of your agent automatically. The alias points to this newly created version. Alternatively, you can point the alias to a previously created version of your agent. Then, you configure your application to make API calls to that alias.

At this stage of the workshop, you have sufficiently modified your agent and it's ready to be deployed to your application. You will now create an alias to point to a version of your agent.

1. Make sure you are on the **DigitalBarista Agent overview** page. If you are not, navigate **Amazon Bedrock > Agents > DigitalBarista**.
    
2. At the top right side of this page, select **Create Alias**
    

![Agent overview create alias](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/agent_create_alias.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

3. For the **Alias name**, name it **DigitalBarista-Alias**. Leave the rest of the settings default. Select **Create Alias**.

![Create alias](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/create_alias.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

4. When it's complete, you will return to the **Agent Overview** page. At the top of the page, right side, you will see **ID**, this is your **Agent ID** Then, Scroll down to the bottom of the page till you see the **Aliases** section. You will see your aliase. Copy and make note of your **Alias ID** and **Agent ID**. You will need these IDs later in the workshop.

![agent id](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/agent_id.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__) ![agent aliase section](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/agent_aliase_section.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

> [!todo]
> Phải thêm 2 cái ID vào xxAPIProxyxx
> 
![[image20.png]]

## IX. Test your Setup

### Congratulations!

You've completed Module 2. However, let's put it all to the test before you move on.

1. You should still be on the **DigitalBarista Agent overview** page. If you are not, navigate **Amazon Bedrock > Agents > DigitalBarista**.
    
2. At the top, left side of the **Agent overview** page, next to the **Create Alias** button is the **Test** button. Select the **Test** button.
    
3. The **Test** column should now appear. On the drop down menu of the test, make sure to select the **Version 1** or the most recent version of your **Agent Alias**.
    

![agent test](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/agent_test.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

4. You can now enter prompts in the user interface provided. ![Agent response test](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/agent_response_test.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

- Example Agent prompts:
    - My name is Bob and I need help finding a drink.
    - Looking for a cold drink that is fruity.
    - Can you recommend a drink that is good in the afternoon?

You may not get a drink recommendation on the first response. The agent may have additional questions to ask.
### Troubleshooting

If you're not getting expected results, there may be a few things to check for:

- Is the **Agent** in a **PREPARED** status?
- Is the **Knowledge base** sync'd with the **Data Source**?
- Did all the PDF files that contain the **Product Data** get uploaded?



---

# Module 3 - Configure and Deploy Frontend App

## I. Configure APIGateway Lambda

Now that we have finished the Agent and Knowledge base setup, it is time to configure the frontend application. The client will follow the logical pathway, **ApiGateway -> Lambda -> Bedrock Agent**. The Lambda will need configured with the **Agent Alias** and **Agent ID** so it knows which agent to invoke.

1. In the AWS console, navigate to the **Lambda** service and select `digital-barista-APIProxy-{Random}`.
    
2. Select the **Configuration** tab and **Environmental Variables** on the left hand side.
    
3. Select **Edit** and replace `AGENT_ALIAS` and `BEDROCK_AGENT_ID` values with th correct values from your _Agent_. ![picture](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/edit_env.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)
    
4. Select **Save**

> [!todo]
> Phải thêm 2 cái ID vào xxAPIProxyxx
>![[image21.png]]

## II. Deploy Frontend Application

Now you are ready to deploy the React application. Navigate back to the command line.

1. From the command line, navigate back to the **bedrock-agents-order-bot-workshop** directory:

```bash
cd ~/bedrock-agents-order-bot-workshop
```

2. You can make sure you're in the correct directory by listing the files and ensure you have the source code files.

```bash
ls
```

![ls of code](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/ls_of_code.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

3. You need to install the the React package dependencies by running following command:

```bash
npm install
```

4. Next, create an environmental variable file that will inject Amazon Cognito and APIGateway variables into React code with the following command:

```bash
npm run create-env
```

5. Verify that a `.env` file exist by listing all files in the directory.

```bash
ls -a
```

![env picture](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/hidden_files.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

6. Now deploy the app to S3 and access via Cloudfront. Run the build and deploy script with following command:

```bash
npm run sync-website
```

7. Scroll up in the command line logs and look for the `CloudfrontURL` output. It should be similar to `CloudfrontURL: 'd-------c0n.cloudfront.net'`. Copy this value and enter into a browser.

![cloudfront cli](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/cloudfronturl_cli.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)
## III. Log in to the Application

1. Durning Cloudformation deployment you should have entered your email address as a parameter and received an email with subject: _**Your temporary password**_ from sender [no-reply@verificationemail.com](mailto:no-reply@verificationemail.com) . Use provided credentials within this email to login. ![picture](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/login.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)
    
2. Create a new password, confirm and select **Change Password**. On verification screen select **Skip** ![picture](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/change_pass.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)

### Navigate App

1. Engage with the Chatbot to select a drink a submit an order The Chatbot follows the flow of instructions and actions given to the Bedrock Agent.
- Get Customer name and look up if they have a profile.
- If profile returned use the data to make a first recommendation.
- Once a drink is selected confirm the pickup location. Possible locations are returned from database based on city.
- Confirm order, then submit to the commerce endpoint (in this case DynamoDB).

1. Once order has been submitted verify it made it to the commerce endpoint by selecting the receipt icon in the top right ![picture](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/overview.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)
### Time to Party!!!

Congratulations! You have built an end to end Generative AI Chatbot Agent: Recommend and Order application.

Please fill out feedback form FORM HERE

----

# Module 4 - Cleanup and Remove Resources

## I. Cleanup product objects from S3

1. Navigate to **Amazon S3** in the **AWS console**. You may need to click **Buckets** on the left hand menu if there isn't a list of S3 buckets. Click on your `digital-barista-bedrockknolwedgebasebucket-{RandomString}` bucket to see its contents. There are 8 product category CSVs that should have been copied. ![bucket domain data](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/bucket_domain_data.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)
    
2. Select all objects and click **Delete**. Type `permanently delete` and click **Delete objects** ![bucket domain data delete](https://static.us-east-1.prod.workshops.aws/3c5f300d-68b0-4f53-b425-2003a434e39b/static/bucket_domain_data-delete.png?Key-Pair-Id=K36Q2WVO3JP7QD&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9zdGF0aWMudXMtZWFzdC0xLnByb2Qud29ya3Nob3BzLmF3cy8zYzVmMzAwZC02OGIwLTRmNTMtYjQyNS0yMDAzYTQzNGUzOWIvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc0NzExNjQ1Nn19fV19&Signature=Ys%7EBzR780hO22lfP2w13zccWOxIfDKYKH5FM%7Ez9SHvfIwIfvcp63ET9cR9DdhLzrwI4ywXo0I4G8N5FQd6Pr09dwaBVTi9iDfAE83pQmALgia5h5E8Al3oRq47ypEXlcXAqhJ-YcmdalRTzjL%7EJ4AatKe4uza3xf23nUWY6qC4TVu7m8HQmGPc2pLfT49sXN9lk8HBjpHe3qRCakSONO2ezgQEjEWor1MQ4V14qJNv4s44a63LzwgcngqbMVXepa9uJI4N-g2l8uH9B0V9ccusa8L1pP5xUkKJxMNaNazi7twKZgYV-Nc1SCUQYHQZ5AMxMrtUPnkxlIUd2fb80jjw__)
    
3. Repeat this process for all objects in the S3 bucket named `digital-barista-{RANDOM}-webui`
    

## II. Remove Cloudformation Stack Resources

1. From the command line, change director to ./backend directory and use AWS SAM to remove AWS resources.

```bash
cd ./backend
sam delete
```

2. Yes to all prompts to delete all resources
## III. Cleanup Bedrock Knowledge Base & Agents

1. Navigate to Bedrock Knowledge bases console
    
2. Select your knowledge base and click **Delete**
    
3. Type `delete` in the input box and click **Delete**
    
4. Navigate to Bedrock Agents and repeat delete process for your agent

