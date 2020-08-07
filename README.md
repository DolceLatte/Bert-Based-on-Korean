# Bert-Based-on-Korean

NLP를 위한 선학습 언어모델 BERT

![Screenshot from 2020-08-07 17-07-11](https://user-images.githubusercontent.com/45285053/89623976-82f34680-d8d0-11ea-8761-a1ec0d5441ce.png)

구글 BERT base multilingual cased의 한국어 성능 한계 -> 다양한 <strong>Korean BERT pre-trained cased</strong> 등장

<h3>한국어 언어 모델</h3>
<li>
  <ol>
  1. ETRI - KorBert</br>
  </ol>
  <ol>
  2. SKT BRAIN - KoBert</br>
  </ol>
  <ol>
  3. BERT multilingual</br>
  </ol>
  <ol>
  4. HanBert - TwoBlock Ai</br>
  </ol>
</li>

Korean BERT들의 성능비교 : 다양한 언어모델간의 차이와 성능을 분석해보자!

<h4>TEST SET</h4>
- NSMC : 네이버 영화 리뷰 긍부정 데이터 </br>
- Korquad1.0</br>
- kakaobrain / KorNLUDatasets</br>

<h5>결과</h5>

<h5>1. NSMC</h5>
- Naver sentiment movie corpus v1.0

This is a movie review dataset in the Korean language.
Reviews were scraped from [Naver Movies](http://movie.naver.com/movie/point/af/list.nhn).

The dataset construction is based on the method noted in [Large movie review dataset](http://ai.stanford.edu/~amaas/data/sentiment/) from Maas et al., 2011.

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
