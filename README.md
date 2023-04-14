# Guide to using Google Cloud Vision OCR code

This is a Python code that uses the Google Cloud Vision OCR API to extract text from images. Here's a step-by-step guide on how to use it:

## Prerequisites
- Make sure you have a Google Cloud account and have set up billing.
- Create a service account with appropriate permissions to use the Cloud Vision API.
- Download the service account credentials in JSON format and save it to the same directory as this Python script.

## Installing required libraries
- This code requires the following libraries to be installed:
  - google-cloud-vision
  - google-auth
  - google-auth-oauthlib
  - google-auth-httplib2
  - tkinter
  - pillow

## Running the code
- Open the Python script in a code editor of your choice.
- Update the credentials file name in the following line of code to match the name of your credentials file:
- Run the Python script in your terminal.

## Using the UI
- Once the script is running, a UI window will appear.
- Click on the "Load Image" button to select an image file from your computer to process.
- Alternatively, click on the "Paste Image" button to paste an image from your clipboard.
- The image will be displayed in the window and the OCR process will begin.
- The extracted text will be displayed in the text box below the image.
- If no text is extracted, a message will be displayed in red text.
- You can turn on or off the printing of the API response payload to the console by clicking on the "Print API Respond On/Off" button. 

## Temporary Folder
- The script will create a temporary directory to save the image files processed.
- The path of this temporary directory will be printed to the console upon running the script.
- You can change the prefix for the temporary directory by modifying the `prefix` argument in the following line of code:

# How to get service account credentials
To create a Google API Service Account, you need to follow these steps:

## Step 1: Create a Google Cloud Platform Project

To create a Google API Service Account, you must have a Google Cloud Platform (GCP) project. If you don't have one already, follow these steps to create a new project:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click the project drop-down in the top navigation bar and click **New Project**.
3. In the **New Project** dialog, enter a project name and select a billing account. Then click **Create**.

## Step 2: Enable the Required API

Before you can create a service account, you need to enable the Google API you want to use. Follow these steps to enable an API:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click the **Navigation menu** and select **APIs & Services** > **Dashboard**.
3. Click the **Enable APIs and Services** button.
4. Search for the API you want to use and click it.
5. Click the **Enable** button.

## Step 3: Create a Service Account

Once you have created a Google Cloud Platform project and enabled the API, you can create a service account:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click the **Navigation menu** and select **APIs & Services** > **Credentials**.
3. Click the **Create credentials** button and select **Service account key**.
4. In the **Create a service account key** dialog, select the service account you want to use, and choose a key type. We recommend choosing the **JSON** key type.
5. Click the **Create** button.

## Step 4: Download and Save the Service Account Key

After you create the service account, you will be prompted to download the service account key. The key is a JSON file that contains your private key and other important information. Follow these steps to download and save the service account key:

1. Click the **Download** button to download the service account key.
2. Save the key in a secure location on your computer.

## Step 5: Grant Access to the Service Account

To allow the service account to access the API, you need to grant it the appropriate permissions. Follow these steps to grant access:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click the **Navigation menu** and select **APIs & Services** > **Credentials**.
3. Find the service account you just created and click the **Edit** button.
4. Click the **Add Member** button.
5. In the **New members** field, enter the email address associated with the service account you just created.
6. In the **Role** field, select the role you want to assign to the service account. For example, if you want to access Google Drive, you can assign the **Editor** role.
7. Click the **Save** button.

## Move the .json file to the same folder where your script is located.
