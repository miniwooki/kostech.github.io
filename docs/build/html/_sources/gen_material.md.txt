# 재료 물성 카드 생성

## 1. Steel 물성 카드 생성
LAMP에서 Steel 물성 카드 생성은 LS-Dyna의 *MAT_PIECEWISE_LINEAR_PLASTICITY(MAT_024) 카드를 생성하는 기능입니다. 해당 기능에서는 MAT_024 카드에 삽입되는 Load curve를 생성하고 LS-Dyna에서 사용가능한 키워드 파일 생성 및 출력을 위한 기능입니다. Load curve는 재료의 시편 인장 시험에서 얻은 raw data를 strain-stress plastic curve를 fitting으로 생성합니다.

### 1.1 입력 패널 UI
LAMP의 상단 아이콘 메뉴에서 ![]() 아이콘을 클릭하면 입력 패널 UI가 우측에 표시됩니다.

![](images/MAT0.png){align=center}

### 1.2 Working directory
Working directory는 Curve Fitting으로 생성되는 데이터가 저장되는 경로를 지정합니다.
:::{admonition} Selection of working directory
:class: tip
`Working directory` 선택은 입력란을 더블 클릭 하여 선택할 수 있습니다.
:::

### 1.3 Material property
MAT_024 카드에 입력될 재료 물성 값을 입력합니다.
:::{admonition} Sync with gradient
:class: tip
`Sync with gradient`를 체크하면 항복점 선택 시 정의되는 elastic line의 기울기 값으로 입력됩니다.
:::

### 1.4 Setup raw data
시편 인장 시험 데이터를 불러오고 항복점을 선택합니다.

Load raw data
: 시험 데이터를 가져오기 위해서 ![](images/MAT1.png) 아이콘을 클릭하고 시험 데이터가 작성된 파일을 선택합니다. \
  지원되는 파일 형식은 다음과 같습니다.

  - *.txt : 데이터의 각 열은 tab으로 구분되어야 합니다.
  - *.csv : 데이터의 각 열이 ,로 구분된 파일입니다.
  - *.xlsx : 일반적으로 엑셀(Excel)에서 사용되는 파일 형식입니다. 
 
 ![](images/MAT2.png){align=center}

 Selection of data
 : 가져올 strain-stress 데이터를 블록 선택한 후에 Data Type을 선택하고 필요에 따라 `Name of Data`를 변경합니다. \
   만약에 선택한 데이터가 strain rate를 가진다면 `Strain Rate`를 입력합니다. 

 :::{caution}
 가져오는 strain-stress 데이터의 각 열은 반드시 서로 인접해야 합니다.
 :::

 :::{admonition} Selection of Data Type
 Curve fitting은 Engineering strain-stress를 사용하여 수행되기 때문에 선택한 데이터는 Engineering strain-stress로 변환됩니다. 변환을 위해서 선택한 데이터가 어떤 형태의 데이터인지를 알아야 하기에 Data Type을 선택합니다.

 - True Strain Stress : 선택한 데이터가 True Strain Stress(진응력)일 경우 선택합니다.
 - Engineering Strain Stress : 선택한 데이터가 Engineering Strain Stress(공칭응력)일 경우 선택합니다.
 - Engineering Strain[%] Stress : 선택한 데이터가 Engineering Strain Stress이면서 Strain이 %단위일 경우 선택합니다.
 - Displacement vs. Force : 선택한 데이터가 Displacement-Force일 경우 선택합니다.

 :::{attention}
 Displacement vs. Force일 경우 Engineering Strain Stress로 변환하기 위해 시편의 Guage Length, Specimen Width, Specimen thickness가 필요합니다. 활성화 되는 아래 입력란에 입력할 수 있습니다.
 :::
 :::