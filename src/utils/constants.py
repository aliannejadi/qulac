data_root = 'data/'
data_mturk_root = data_root + 'mturk/'
data_web_track_path = data_root + 'web_track/'
data_mturk_q_facet_v1_path = data_mturk_root + 'question-facet/v1/'
data_mturk_q_facet_v11_path = data_mturk_root + 'question-facet/v11/'
data_mturk_q_path = data_mturk_root + 'questions/'
data_mturk_answer_path = data_mturk_root + 'answers/'


output_path = 'output/'
output_final_data_path = output_path + 'acqua/'
output_q_for_facet_path = output_path + 'q_for_facet/'
output_mturk_answer_HIT_path = output_path + 'mturk_answer_HIT/'
output_mturk_q_facet_matching = output_path + 'q_facet_matching/'

final_data_file_name = 'clqu.csv' 
final_data_path = output_final_data_path + final_data_file_name

num_q_per_topic = 12
max_facets_per_topic = 6

topic_file = 'topics_facets_with_qrel.csv'

# for questions hit
num_q_per_row = 6
rows_per_topic = 2

# for answers hit
answer_banned_workers_file_name = 'banned_workers.csv'

# mturk columns

# columns 
facet_cols = ['Input.facet{}'.format(x) for x in range(max_facets_per_topic)]
relq_cols = ['Answer.relevant_questions_{}'.format(x) for x in range(max_facets_per_topic)]
needq_cols = ['Answer.need_question_{}'.format(x) for x in range(max_facets_per_topic)]
q_cols = ['Input.question{}'.format(x) for x in range(num_q_per_topic)]
new_q_cols = ['Answer.new_question_{}'.format(x) for x in range(max_facets_per_topic)]

initial_cols = ['WorkerId', 'WorkTimeInSeconds','Input.topic_id', 'Input.query']

# for aws api
aws_region_name = 'us-east-1'
aws_access_key_id = 'AKIAJAJQ6ZEHQFOSQNUA'
aws_secret_access_key = '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'
aws_endpoint_url = 'https://mturk-requester.us-east-1.amazonaws.com'
aws_client_name = 'mturk'

# evaluation
runs_path = 'runs/'
eval_temp_path = 'tmp/'
eval_temp_run_file_name = 'run'
eval_temp_run_path = eval_temp_path + eval_temp_run_file_name
eval_temp_qrel_file_name = 'qrel'
eval_temp_qrel_path = eval_temp_path + eval_temp_qrel_file_name
faceted_qrel_path = output_path + 'faceted.qrel'

# ranklib
ranklib_root = "Ranklib/"
ranklib_data = ranklib_root + "data/"
ranklib_features = ranklib_root + "features/"
ranklib_models = ranklib_root + "models/"
ranklib_rankings = ranklib_root + "rankings/"
