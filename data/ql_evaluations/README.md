# Qulac
A dataset on asking Questions for Lack of Clarity in open-domain information-seeking conversations.

## File Download

You can download `eval_hist012_dict.tar.gz` here: [http://ciir.cs.umass.edu/downloads/qulac/data/ql_evaluations/eval_hist012_dict.tar.gz](http://ciir.cs.umass.edu/downloads/qulac/data/ql_evaluations/eval_hist012_dict.tar.gz)
  

## File Format
### `eval_hist012_dict.tar.gz`:

This file contains the evaluation results of all possible combinations of questions and answers with 1, 2, and 3 turns. The retrieval is done using a modified QL model (see [1]) and evaluated on a modified TREC qrel file. The metrics are nDCG@1,3,5,10,20; P@1,3,5,10,20; MRR@100. The dictionary is formatted as follows:

	{ <metric_identifier> : <record_id> : <value> }
	
Here is a sample data:

	{'MRR100': {'20-2-1-0': 0.0,
		  '20-2-1-1': 0.0,
		  '20-2-10-0': 0.0,
		  '20-2-10-1': 0.0,
		  '20-2-11-0': 0.0,
		  '20-2-11-1': 1.0,
		  '20-2-12-0': 0.0,
		  '20-2-12-1': 0.0,
		  ...},
	  
	 'NDCG20': {'20-2-1-0': 0.0,
		 '20-2-1-1': 0.0,
		 '20-2-10-0': 0.0,
		 '20-2-10-1': 0.0,
		 '20-2-11-0': 0.0,
		 '20-2-11-1': 0.36252395084997224,
		 '20-2-12-0': 0.0,
		 '20-2-12-1': 0.0,
		 '20-2-13-0': 0.0,
		 '20-2-13-1': 0.24356187958225833,
		 '20-2-14-0': 0.0,
		 '20-2-14-1': 0.10773341865761957,
		 ...},
	 ...
	}
	 
**NOTE:** Relevant codes and qrel files to reproduce this `dict` will be added to the repository later.

## Citation

Please consider citing the following paper if you use Qulac in your research:

	@inproceedings{AliannejadiSigir19,
	    author    = {Aliannejadi, Mohammad and Zamani, Hamed and Crestani, Fabio and Croft, W. Bruce},
	    title     = {Asking Clarifying Questions in Open-Domain Information-Seeking Conversations},
	    booktitle = {International {ACM} {SIGIR} Conference on Research and Development in Information Retrieval (SIGIR)},
	    series    = {{SIGIR '19}},
	    location  = {Paris, France},          
	    year      = {2019}
  	}
  	
## Acknowledgments

This work was a joint effort by Università della Svizzera italiana (USI), Lugano, Switzerland and University of Massachusetts, Amherst, MA, USA. Thanks to the expert annotators and crowd workers for their invaluable help in annotating Qulac.