from libc.math cimport log


def ql_score_f(float q_score, float dfreq, float mu, float doc_len, float nq, float total_terms):
    cdef float d_score = dfreq / (mu + doc_len)
    d_score += (mu / (mu + doc_len)) * (nq / total_terms)
    if d_score > 0:
        return (q_score * log(d_score))
    else:
#         print('This terms returns zero document frequency: ', t)
        return 0
