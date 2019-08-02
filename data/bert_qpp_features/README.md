# Qulac
A dataset on asking Questions for Lack of Clarity in open-domain information-seeking conversations.

## File Download

You can download `bert_qpp_dict.tar.gz` here: [http://ciir.cs.umass.edu/downloads/qulac/data/bert_qpp_features/bert_qpp_dict.tar.gz](http://ciir.cs.umass.edu/downloads/qulac/data/bert_qpp_features/bert_qpp_dict.tar.gz)

## File Format

### `bert_qpp_dict.tar.gz`:

We have provided the features and representations that we used in [1] for reproducibility. Hence, this file contains a `dict` as follows:

	<record_id> : {
			'query_facet_id': <same as topic_facet_id in qulac.json>,
			'query': <BERT representation of the query (topic)>,
			'question': <BERT represenation of the question>,
			'history_list': [
					<BERT representation of the first question answer pair in the context>,
					<BERT representation of the second question answer pair in the context>,
					<BERT representation of the third question answer pair in the context>
					],
			'history_len': <number of turns in the conversation history (context)>,
			'scores': <the scores of top ranked documents after running the modified QL using query, history, and question>,
			'scores_std': <standard deviation of top k scores>
		}
					
Below we see a sample:

	{ '1-2-2-1-1': 
		{
			'history_len': 1,
			'history_list': [[0.12686,
					   -0.60192,
					   -0.208874,
					   0.001408,
					   -0.036675,
					   0.023856,
					   -0.274937,
					   ...]],
			'query': 	[-0.607881,
					  -0.918204,
					  -0.162166,
					  -0.850832,
					  0.403656,
					  0.551275,
					  0.141782,
					  0.89388,
					  0.517192,
					  ...],
			'query_facet_id': '1-2',
			'question': 	[-0.683592,
					  -0.436706,
					  -0.881163,
					  -0.154672,
					  0.321163,
					  -0.110311,
					  -0.010973,
					  1.051107,
					  0.244392,
					  ...],
			'scores': 	[-5.979888569396179,
					  -6.4430787788018495,
					  -6.444356256703669,
					  -6.4445699080820775,
					  -6.444756161165571,
					  -6.517334331640069,
					  -6.588618185924115,
					  -6.618846047988905,
					  -6.627880109313763,
					  ...],
			'scores_std': 	[0.0,
					  0.32752493804996663,
					  0.2677925299530175,
					  0.23205747316634495,
					  0.20764307553239575,
					  0.19770034752952462,
					  0.1971001297433477,
					  0.19699259692169363,
					  ...]
		}
		...
	}
						  

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
