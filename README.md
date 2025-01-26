# SliTraNet_Implementation

This is a fork of the respository SliTraNet (found [here](https://github.com/asindel/SliTraNet)), which contains the source code to the conference article "SliTraNet: Automatic Detection of Slide Transitions in Lecture Videos using Convolutional Neural Networks" accepted at OAGM Workshop 2021 [here](https://arxiv.org/pdf/2202.03540.pdf)

## Important to Note:
This fork is for **personal testing** and exploration of SliTraNet. This is **NOT intended to be merged into the main branch of original repository**

## Key Changes
- Replace deprecated `decord` library functionalities using alternative methods from `MoviePy` and `cv2` (`requirements.txt` is updated)
- Make runs compatible with MacOS MPU (removed cuda usage)
- Added `visualise_predictions.ipynb` to visualise and verify results of SliTraNet. Due to data privacy, no outputs are included in this folder.

- Folder Structure:
	- `../videos`: contain videos for framework testing and bounding box labels (text files as specified in original repository)
	- `../weights` contain model weights, taken from the original repository [here](https://drive.google.com/drive/folders/1aQDVplbbpt-zgH2O1q7685AZ1hl0BsVV?usp=sharing).

## To Run Model
- ensure folder structure is as specified as above
- modify parameters (optional)
- run `test_SliTraNet.py`
- run `visualise_predictions.ipynb` 

## Citations
@misc{sindel2022slitranet,
		title={SliTraNet: Automatic Detection of Slide Transitions in Lecture Videos using Convolutional Neural Networks},
		author={Aline Sindel and Abner Hernandez and Seung Hee Yang and Vincent Christlein and Andreas Maier},
		year={2022},
		eprint={2202.03540},
		archivePrefix={arXiv},
		primaryClass={cs.CV}
	  }
