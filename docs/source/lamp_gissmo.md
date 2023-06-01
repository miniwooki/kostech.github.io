# LAMP GISSMO

LAMP GISSMO는 ls-dyna에서 재료의 파단을 재현하기 위해 사용되는 GISSMO(Generalized Incremental Stress State dependent damage MOdel) 물성을 생성할 수 있는 인터페이스를 제공합니다. LAMP GISSMO를 이용하기 위해서는 다음과 같은 항목들이 필요합니다.

- LS-Dyna License and Solver
- LS-OPT ([LS-Dyna 최적화 도구](http://www.kostech.co.kr/ls-opt))
- 최소 3개 이상의 재료 시편 모델 (ex. Uniaxial, Shear, Norch, Biaxial 등등)
- 각 재료 시편 모델의 Force-Displacement 시험 Curve 데이터

LAMP GISSMO는 총 5단계로 구성되며 각 단계에서 수행되는 내용은 다음과 같습니다.

Step 1
: 준비된 시편 모델들을 불러오고 LS-OPT를 이용하여 최적화할 파라미터들의 정보를 입력

Step 2
: Step1 에서 입력한 시편 모델 및 변수 정보를 바탕으로 LS-OPT 최적화 시뮬레이션을 수행

Step 3
: Step2 에서 수행한 최적화 시뮬레이션 결과에서 최적의 결과를 선택하고 Fracture 및 Instability Curve를 생성

Step 4
: Step4에서는 모델의 메쉬 크기에 따른 결과 차이를 보정하기 위해 메쉬 정규화를 진행합니다. 메쉬 정규화를 위해 하나의 Reference 시편 모델이 선택되며, Reference 모델과 형상을 동일하면서 다른 메쉬 크기를 가지는 시편 모델이 요구됩니다. 

Step 5:
: Step1~4까지 진행된 내용을 체크하고 LS-Dyna에서 사용 가능한 GISSMO 파단 물성 카드를 생성합니다.