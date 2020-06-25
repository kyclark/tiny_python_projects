TAG = kyclark/tiny_python_projects:0.2.0

img:
	docker build --tag=$(TAG) .

shell:
	docker run -it $(TAG) bash

push: 
	docker push $(TAG)
