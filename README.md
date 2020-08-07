# Bert-Based-on-Korean

NLP를 위한 선학습 언어모델 BERT

![Screenshot from 2020-08-07 17-07-11](https://user-images.githubusercontent.com/45285053/89623976-82f34680-d8d0-11ea-8761-a1ec0d5441ce.png)

구글 BERT base multilingual cased의 한국어 성능 한계 -> 다양한 <strong>Korean BERT pre-trained cased</strong> 등장

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

<h5>1. NSMC</h5>
<table>
  <tr>
    <td>MODEL</td><td>ACCURACY</td>
  </tr>
  <tr>
    <td>BERT-MULTILINGUAL-cased</td><td>0.86</td>
  </tr>
  <tr>
    <td>KorBert</td><td>0.8946</td>
  </tr>
  <tr>
    <td>KoBert</td><td>0.901</td>
  </tr>
</table>
