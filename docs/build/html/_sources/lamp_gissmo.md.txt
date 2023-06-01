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

Step 5
: Step1~4까지 진행된 내용을 체크하고 LS-Dyna에서 사용 가능한 GISSMO 파단 물성 카드를 생성합니다.

## GISSMO Interface Panel

LAMP GISSMO의 입력 패널의 제일 상단에는 작업 디렉토리(Working Directory)를 설정하는 항목이 있습니다. 작업 디렉토리에는 과정중에 생기는 파일들이 저장되는 경로이며, 특정 경로에서 불러오는 시편모델등의 데이터는 따로 복사되어 저장되지 않습니다.

![](images/gissmo/gissmo0.png)

## Step 1

Step 1에서는 준비된 시편 모델들을 추가하고 설계 파라미터들의 범위를 입력합니다. \
추가된 모든 시편 모델에 대해 다음의 항목들을 선택 및 입력합니다.

- Specimen : 우측 아이콘 버튼을 클릭하고 시편 모델의 메인 키워드(Keyword) 파일을 선택합니다. 시편 모델을 정상적으로 읽었다면 다음의 과정들이 진행됩니다. 

    - Keyword 파일에서 *DEFINE_CURVE 카드를 찾고 Curve의 ID를 LCSS ID 항목에 추가합니다.
    - Keyword 파일에서 *DATABASE_HISTORY_NODE_ID 카드를 찾고 입력된 두 개의 노드 정보로 부터 Gauge length를 계산해 G. Length 항목에 입력합니다. 

    :::{caution}
    시편 모델에는 해석 과정중에 변위가 계산될 수 있도록 *DATABASE_HISTORY_NODE_ID 카드를 이용해 변위 계산을 위한 두 개의 노드 ID를 설정해야 합니다.
    :::

- T. Curve : 우측 폴더 모양의 아이콘을 클릭하고 추가한 시편 모델의 Force-Displacement 시험 데이터가 정의된 파일을 선택합니다. 좌측 그래프 모양 아이콘으로 선택한 데이터를 그래프로 확인 할 수 있습니다.

- LCSS ID : 시편 모델을 불러오면서 인식된 *DEFINE_CURVE들의 ID 항목이 추가되며, *MAT_PIECEWISE_LINEAR_PLASTICITY 카드에 사용될 Curve의 ID를 선택합니다.

- G. Length :  *DATABASE_HISTORY_NODE_ID 카드에 정의된 두 노드 정보로 부터 계산된 Gauge length를 표시합니다.

- Direction : 시편이 인장되는 방향을 설정합니다.

- F. Factor : Force Factor를 입력하는 항목으로 Biaxial 시편 모델에만 입력된 값이 사용됩니다.

- Ref. Size : 시편 모델에서 변위를 계산하는 요소의 사이즈를 입력합니다.

- DMGEXP(Exponent for nonlinear damage accumulation) : GISSMO 재료 모델의 DMGEXP 파라미터의 설계 범위를 입력합니다.

- FADEXP(Exponent for damage-related stress fadeout) : GISSMO 재료 모델의 FADEXP 파라미터의 설계 범위를 입력합니다.

- Fracture : 해당 시편의 파단에 대한 equivalent plastic strain을 결정하기 위한 파라미터의 설계 범위를 입력합니다.

- Instability : 해당 시편의 Critical equivalent plastic strain을 결정하기 위한 파라미터의 설계 범위를 입력합니다.

:::{tip}
Specimen 항목의 ComboBox에 추가된 시편 모델들을 변경할 수 있습니다. 변경 시 선택된 시편 모델의 입력 정보로 변경됩니다. \
Specimen 항목의 우측 휴지통 아이콘을 통해 추가된 시편 모델을 제거 할 수 있습니다.
:::

![](images/gissmo/gissmo1.png)