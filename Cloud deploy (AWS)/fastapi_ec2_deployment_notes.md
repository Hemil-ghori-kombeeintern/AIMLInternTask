# Deploy FastAPI to AWS EC2 Using an Existing Docker Hub Image

## Flow

**Simple FastAPI application → Docker image → AWS EC2**

This guide uses the deployment notes provided for the existing project.
It does not recreate the FastAPI application or rebuild the Docker
image.

------------------------------------------------------------------------

## Step 1 --- Find the Docker repository

Find the Docker image repository and tag in Docker Hub.

**Example image:**

``` text
hemil124/fastapi-docker-cicd:latest
```

General image format:

``` text
dockerhub-username/repository-name:latest
```

------------------------------------------------------------------------

## Step 2 --- Launch your EC2 instance

1.  Open the [Amazon EC2 Console](https://console.aws.amazon.com/ec2/).
2.  Create an instance with the following settings:

  Setting            Value
  ------------------ ------------------------
  Name               `ci-cd-fastapi-server`
  Operating system   Ubuntu
  Instance type      `t3.micro`
  Key pair           `.pem` key pair
  Network settings   SSH and HTTP

3.  Review the settings and launch the instance.

> **Free-plan reminder:** Confirm in your AWS account that the selected
> instance type, region, storage, networking, and other resources are
> eligible for your current free offer. Free eligibility and charges
> depend on account terms and usage.

------------------------------------------------------------------------

## Step 3 --- Connect to your EC2 instance from Windows Terminal

1.  On your Windows computer, open PowerShell.
2.  Go to the directory where you saved your downloaded `.pem` key file.
3.  Run the SSH command:

``` bash
ssh -i "fastapi-key.pem" ec2-user@YOUR_PUBLIC_IP
```

Replace `YOUR_PUBLIC_IP` with the public IP address of your EC2
instance.

------------------------------------------------------------------------

## Step 4 --- Install Docker on Ubuntu

Run the following commands on the EC2 instance:

``` bash
sudo apt update

sudo apt install -y docker.io

sudo systemctl enable --now docker

sudo docker --version

```

> **Check the operating system and commands:** These notes specify
> Ubuntu, but the `dnf` commands and `ec2-user` account are commonly
> associated with Amazon Linux. Ubuntu normally uses `apt` and the
> default account is commonly `ubuntu`. If you launched Ubuntu, use the
> correct Ubuntu SSH username and Docker installation commands for that
> OS. If you intend to use the commands above as written, verify that
> the selected AMI is compatible with them.

------------------------------------------------------------------------

## Step 5 --- Pull and run your existing Docker image

Pull the image from Docker Hub:

``` bash
sudo docker pull YOUR_DOCKERHUB_USERNAME/YOUR_IMAGE:latest
```

For the image listed in Step 1, the pull command is:

``` bash
sudo docker pull hemil124/fastapi-docker-cicd:latest
```

Then run the FastAPI container:

``` bash
sudo docker run --name ci-cd-fastapi --restart unless-stopped -p 8000:8000 hemil124/fastapi-docker-cicd:latest
```

Check whether the container is running:

``` bash
docker ps
```

If you encounter a Docker permission error, try prefixing Docker
commands with `sudo`, for example:

``` bash
sudo docker ps
```

------------------------------------------------------------------------

## Step 6 --- Open your FastAPI application

Open the Swagger documentation in your browser:

``` text
http://YOUR_PUBLIC_IP:8000/docs
```

Replace `YOUR_PUBLIC_IP` with the public IP address of your EC2
instance.

Make sure the EC2 security group permits inbound TCP traffic on port
`8000` from the IP addresses that need to access the API. The SSH rule
should be restricted to **My IP** for the setup described in the
deployment notes.

------------------------------------------------------------------------

## Live URL

This is a live URL:

<http://13.232.29.60:8000/docs>

>Public ip change every time so replace it
------------------------------------------------------------------------
