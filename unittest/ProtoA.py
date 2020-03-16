import spacy

activated = spacy.prefer_gpu()
nlp = spacy.load('en_core_web_lg')

def segment_phrase(sentence):
  res = []
  doc = nlp(sentence)
  root = doc[:].root
  
  def check_conj(rt):
      for token in rt.rights:
          if token.dep_ not in ['cc', 'conj', 'punct']:
              return False
          if token.dep_ == 'conj':
              break
      return True
  
  def split(rt):   
      if rt.pos_ == 'PUNCT' or rt.pos_ == 'CCONJ' or rt.pos_ == 'SYM':
          return []
      ret = ['']
      if not (rt.pos_ == 'VERB' and rt.dep_ not in ['xcomp', 'ccomp']):
          for token in rt.lefts:
              left_ret = split(token)
              if len(left_ret) == 0:
                  continue
              ret_ = [x + y + " " for x in ret for y in left_ret]
              ret = ret_
      
      ret_ = [x + rt.text for x in ret]
      ret = []
    
      flag = False
      for token in rt.rights:
          right_ret = split(token)
          
          if len(right_ret) == 0:
              continue
          
          if token.dep_ == 'conj' and rt.pos_ == token.pos_ and check_conj(rt):
              
              if not flag:
                  for sent in right_ret:
                    
                      right = doc[token.left_edge.i : token.i+1].text
                      if right in sent:
                          ret.extend([sent.replace(right, x) for x in ret_])
                  flag = True
              if token.pos_ != 'VERB':
                  ret.extend(right_ret)
              ret_ = ret
              
          else:
              ret = [x + " " + y for x in ret_ for y in right_ret]
              ret_ = ret
      ret = ret_
    
      if rt.pos_ == 'VERB' and rt.dep_ not in ['xcomp', 'ccomp']:
          res.extend(ret)
          if rt.dep_ == 'conj' and rt.head.pos_ == 'VERB' and check_conj(rt.head):
              return ret
          else:
              return []
      else:
          if rt.i == root.i:
              res.extend(ret)
          return ret
  return res