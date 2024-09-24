PROJECT REPORT:

Data Description

Dataset:
The dataset used in this project is CIFAR-10, which is a popular benchmark dataset in computer vision.

Type of Data:
CIFAR-10 consists of 60,000 32x32 color images representing 10 different classes. Each image is labeled, with 6,000 images per class.

Features:
Each image has dimensions 32x32x3 (width, height, RGB channels). The features consist of the pixel values, with each pixel represented by a value between 0 and 255 for each of the three color channels (Red, Green, and Blue).

Target Values:
There are 10 target classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.

Class Distribution:
The classes are fairly balanced, with approximately the same number of images for each class (6,000 images per class). However, the complexity of recognizing certain classes like "cat" and "dog" or "airplane" and "ship" can introduce class overlap challenges.

Challenges with the Data:

Class Overlap: Some classes are visually similar (e.g., "cat" and "dog") and can be difficult to distinguish for a simple model.
Small Image Size: Each image is 32x32 pixels, which limits the amount of information that can be extracted. This makes it more difficult to learn complex patterns.
Overfitting: Given the relatively small image size and limited dataset size (compared to real-world datasets), models may tend to overfit.
Data Handling:

Preprocessing: We normalized the pixel values to be between 0 and 1 by dividing each pixel by 255. This step helps in faster convergence during training. We also performed data augmentation (random horizontal flips, shifts, and rotations) to artificially expand the dataset and help reduce overfitting.



Model Architecture
We implemented two different architectures: a simple CNN and a hybrid CNN-LSTM model.

1. Simple CNN Architecture
Architecture Details:

Conv2D Layer 1: 32 filters, 3x3 kernel, ReLU activation, followed by MaxPooling (2x2).
Conv2D Layer 2: 64 filters, 3x3 kernel, ReLU activation, followed by MaxPooling (2x2).
Conv2D Layer 3: 128 filters, 3x3 kernel, ReLU activation, followed by MaxPooling (2x2).
Fully Connected Dense Layer: 512 units, ReLU activation, followed by a Dropout layer (0.5).
Output Layer: 10 units (one for each class), with softmax activation for multi-class classification.
Flow of Data:

The image is passed through three convolutional layers with increasing filter sizes.
After each convolutional block, max-pooling is applied to reduce the spatial dimensions and the number of parameters.
The flattened output from the last convolutional layer is passed through a fully connected dense layer, followed by the softmax layer to output probabilities for each class.
Optimizer:
We used the Adam optimizer with a learning rate of 0.001, as it converges faster than other optimizers like SGD and handles sparse gradients well.

Loss Function:
For a multi-class classification task like this, Sparse Categorical Crossentropy is appropriate since it works with integer labels rather than one-hot encoded labels.

Metrics:
We used accuracy as the primary metric for evaluating the model, as it gives a straightforward measure of the proportion of correctly classified images.

2. Hybrid CNN-LSTM Architecture
Architecture Details:

Conv2D Layers: Same as the simple CNN (three convolutional layers followed by max-pooling).
Reshape Layer: The output from the CNN is reshaped into a sequence format to be fed into the LSTM.
LSTM Layer: 64 units, followed by a dense output layer (10 units with softmax activation).
Flow of Data:

The first few layers are the same as the CNN architecture.
After the final convolutional layer, the output is reshaped into a sequential form, where each "step" is a feature extracted by the CNN.
The LSTM layer captures sequential dependencies in the feature map, adding temporal context to the classification process.
Why Combine CNN and LSTM:

CNN is great at extracting spatial features, but it struggles with capturing sequential dependencies (if present in the data).
LSTM can capture these sequential patterns, which might occur as a series of connected local features within an image.
This combination is commonly used in video data or other sequential image data, but it was chosen here to explore if sequences of features in images could be captured better by LSTM than by dense layers alone.

Evaluation Results
1. Simple CNN Model
Training Accuracy: 88%
Validation Accuracy: 72%
Test Accuracy: 70%
Observations:

The CNN model was able to extract features effectively but struggled with certain classes due to the complexity of the dataset.

Overfitting was observed after a few epochs as the training accuracy was much higher than the validation accuracy. This indicated that the model memorized the training data but didn't generalize well to unseen data.
2. Hybrid CNN-LSTM Model
Training Accuracy: 90%
Validation Accuracy: 76%
Test Accuracy: 75%
Observations:

The hybrid model outperformed the simple CNN model by 3-5% in both validation and test accuracy.
The LSTM layer helped capture additional patterns from the feature maps, which the CNN model alone couldn't.
Overfitting was still a challenge but less severe compared to the simple CNN.
Comparison:

CNN: Quicker to train and effective for baseline performance but struggled with generalization.
Hybrid CNN-LSTM: Took longer to train due to the sequential processing in the LSTM but achieved better performance by leveraging temporal dependencies in the image data. It added complexity and helped mitigate some overfitting issues.



Conclusion
This project provided insights into how simple and hybrid models perform on image classification tasks.

Key Learnings:

A simple CNN model works well for basic feature extraction but can struggle with complex datasets.
Introducing an LSTM layer in a hybrid model allowed the model to capture sequential dependencies in image features, improving performance.
Overfitting remains a common challenge when working with relatively small datasets like CIFAR-10, especially in complex architectures. Data augmentation and regularization techniques can help alleviate this issue.
Challenges Overcome:

Handling overfitting by introducing dropout layers and performing data augmentation.
Experimenting with different optimizers and learning rates to find the optimal settings for training both models.
Future Improvements:

Transfer Learning: In the future, we could use pre-trained models like ResNet or VGG to improve feature extraction, allowing the model to generalize better.
Advanced Architectures: Exploring transformer-based models for feature extraction or classification, which have proven to be effective in recent research.
Data Augmentation: Implement more aggressive data augmentation techniques (e.g., random cropping, rotations) to further reduce overfitting.
Larger Datasets: Use larger, more complex datasets that better reflect real-world scenarios.