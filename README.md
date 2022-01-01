# Block Predication

## Objectives

In this project, our objective was to classify a block from a document that was segmented into several blocks.

The possible classes are as follows :
- Text
- Horizontal Line
- Picture
- Vertical Line
- Graphic

## Achievement

So, based on a provided block dataset, we were able to generate a model with an accuracy of up to 97.23%.

Therefore, we have integrated our model to an API with DJango, which implements the model according to the parameters of a given bloc, being the following:

- height : Height of the block
- length : Length of the block
- blackpix : Total number of black pixels in the original bitmap of the block
- blackand : Total number of black pixels in the bitmap of the block after RLSA
- wb_trans : Number of white-black transitions in the original bitmap of the block

## Tuorial for the API

To start the API, follow these steps:

- Download the project
- Open a command prompt at the project location "block_python_project\block_python_project"
- Activate the virtual environment by typing "venv\Scripts\activate"
- Type "python manage.py runserver" to run the API
- Open any browser
- Enter URL "http://127.0.0.1:8000/" to access to the API

