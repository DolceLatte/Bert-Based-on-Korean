# Bert-Based-on-Korean

NLP를 위한 선학습 언어모델 BERT

구글 BERT base multilingual cased의 한국어 성능 한계 -> 다양한 Korean BERT pre-trained cased 등장

<h3>한국어 언어 모델</h3>
1. ETRI - KorBert</br>

2. SKT BRAIN - KoBert</br>

3. BERT multilingual</br>

4. HanBert - TwoBlock Ai</br>


Korean BERT들의 성능비교 : 다양한 언어모델간의 차이와 성능을 분석해보자!

<h4>TEST SET</h4>
- NSMC : 네이버 영화 리뷰 긍부정 데이터 
- Korquad1.0
- kakaobrain / KorNLUDatasets

결과 

1. NSMC
<table>
  <td>
    <tr>MODEL</tr><tr>ACCURACY</tr>
  </td>
  <td>
    <tr>BERT-MULTILINGUAL-cased</tr><tr>0.86</tr>
  </td>
  <td>
    <tr>KorBert</tr><tr>0.8946</tr>
  </td>
  <td>
    <tr>KoBert</tr><tr>0.901</tr>
  </td>
</table>
