## Environment Setup
- `cd server`
- `pip install virtualenv`
- `virtualenv djangoenv`
- `source djangoenv/bin/activate`
- `python3 -m pip install -U -r requirements.txt`
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

## Run Server
- `python3 manage.py runserver`

## Frontend
- `cd server/frontend`
- `npm install`
- `npm run build`

## Docker
This runs the Mongo Express server, with Mongoose to provide API endpoints
- `cd server/database`
- `docker build . -t nodeapp`
  - Run command if there are changes made to data/app.js
- `docker-compose up`

## IBM Cloud Engine Deployment
This deploys the Sentiment Analyzer microservice on Code Engine
- `cd server/djangoapp/microservices`
- `docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer`
- `docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer`
- `ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000`
- Open `djangoapp/.env` and replace the code engine deployment URL with the deployment URL, including the / at the end of the URL `sentiment_analyzer_url=<your code engine deployment> url`

## Containerize full application
- `docker build -t us.icr.io/${SN_ICR_NAMESPACE}/dealership .`
- `docker push us.icr.io/${SN_ICR_NAMESPACE}/dealership`
- `kubectl apply -f deployment.yaml`
- `kubectl port-forward deployment.apps/dealership 8000:8000`
  - If error: `kubectl rollout restart deployment dealership`, then try port forwarding again
  - View pods: `kubectl get pods`

## Deployment URL from Kubernetes cluster
- https://jeremycheong-8000.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/
