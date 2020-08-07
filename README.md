# Bert-Based-on-Korean

NLP를 위한 선학습 언어모델 BERT

![Screenshot from 2020-08-07 17-07-11](https://user-images.githubusercontent.com/45285053/89623976-82f34680-d8d0-11ea-8761-a1ec0d5441ce.png)

구글 BERT base multilingual cased의 한국어 성능 한계 -> 다양한 <strong>Korean BERT pre-trained cased</strong> 등장

<h3>한국어 언어 모델</h3>
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

Korean BERT들의 성능비교 : 다양한 언어모델간의 차이와 성능을 분석해보자!

## TEST SET 및 실험 결과
- NSMC : 네이버 영화 리뷰 긍부정 데이터 </br>
- Korquad1.0</br>
- kakaobrain / KorNLUDatasets</br>

<h5>1. NSMC</h5>
- Naver sentiment movie corpus v1.0

This is a movie review dataset in the Korean language.
Reviews were scraped from [Naver Movies](http://movie.naver.com/movie/point/af/list.nhn).

The dataset construction is based on the method noted in [Large movie review dataset](http://ai.stanford.edu/~amaas/data/sentiment/) from Maas et al., 2011.
### Quick peek

    $ head ratings_train.txt
    id      document        label
    9976970 아 더빙.. 진짜 짜증나네요 목소리        0
    3819312 흠...포스터보고 초딩영화줄....오버연기조차 가볍지 않구나        1
    10265843        너무재밓었다그래서보는것을추천한다      0
    9045019 교도소 이야기구먼 ..솔직히 재미는 없다..평점 조정       0
    6483659 사이몬페그의 익살스런 연기가 돋보였던 영화!스파이더맨에서 늙어보이기만 했던 커스틴 던스트가 너무나도 이뻐보였다  1
    5403919 막 걸음마 뗀 3세부터 초등학교 1학년생인 8살용영화.ㅋㅋㅋ...별반개도 아까움.     0
    7797314 원작의 긴장감을 제대로 살려내지못했다.  0
    9443947 별 반개도 아깝다 욕나온다 이응경 길용우 연기생활이몇년인지..정말 발로해도 그것보단 낫겟다 납치.감금만반복반복..이드라마는 가족도없다 연기못하는사람만모엿네       0
    7156791 액션이 없는데도 재미 있는 몇안되는 영화 1

#### *Accuracy
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
