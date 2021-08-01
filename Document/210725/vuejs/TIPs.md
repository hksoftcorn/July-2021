# TIL - Vue

## 1. 기본기

### 한국어 input 이벤트 처리 & 체크박스

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <!-- 한글의 경우 1번 케이스를 사용해야 함 -->
    <!-- https://kr.vuejs.org/v2/guide/forms.html -->
    <h2>1. Input -> Data</h2>
    <h3>{{ myMessage }}</h3>
    <input @input="onInputChange" type="text">
    <hr>

    <h2>2. Input <-> Data</h2>
    <h3>{{ myMessage2 }}</h3>
    <input v-model="myMessage2" type="text">
    <hr>

    <h2>3. Checkbox</h2>
    <input type="checkbox" id="checkbox" v-model="checked">
    <label for="checkbox">{{ checked }}</label>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        myMessage: '',
        myMessage2: '',
        checked: true,
      },
      methods: {
        onInputChange: function (event) {
          this.myMessage = event.target.value
        },
      }
    })
  </script>
</body>
</html>

```

### v-bind 여러가지 활용

```vue
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .active {
      color: red;
    }

    .my-background-color {
      background-color: yellow;
    }
  </style>
</head>
<body>
  <div id="app">
    <!-- 속성 바인딩 -->
    <img v-bind:src="imageSrc">
    <img :src="imageSrc">

    <hr>

    <!-- 클래스 바인딩 -->
    <div :class="{ active: isRed }">클래스 바인딩</div>

    <h2 :class="[activeRed, myBackground]">
      Hello Vue.js
    </h2>

    <hr>

    <!-- 스타일 바인딩 -->
    <ul>
      <li v-for="todo in todos" :class="{ active: todo.isActive }" :style="{ fontSize: fontSize + 'px' }">
        {{ todo }}
      </li>
    </ul>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        imageSrc: 'https://picsum.photos/200/300/',
        isRed: true,
        activeRed: 'active',
        myBackground: 'my-background-color',
        todos: [
          { id: 1, title: 'todo 1', isActive: true },
          { id: 2, title: 'todo 2', isActive: false },
        ],
        fontSize: 10,
      }
    })
  </script>
</body>
</html>

```

### computed & watch

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <p>a: {{ a }}</p>
    <p>Computed: a의 제곱은 {{ square }} 입니다.</p>
    <p>Watch: a는 {{ increase }} 만큼 증가했습니다.</p>
    <input type="number" v-model.number="delta">
    <button @click="a += delta">a 증가</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        a: 0,
        delta: 0,
        increase: 0,
      },
      computed: {
        square: function () {
          console.log('Computed !')
          return this.a**2
        }
      },
      // a가 변경되면 변경된 값을 콜백함수의 첫번째 인자로 전달하고 이전 값을 두번째 인자로 전달
      // computed는 새 프로퍼티를 생성하지만 watch는 아무 프로퍼티도 생성하지 않고 익명함수는 단순히 콜백함수 역할만 함
      // watch에 명시된 프로퍼티는 감시할 대상을 의미할 뿐임
      watch: {
        a: function (newValue, oldValue) {
          console.log('Watch !')
          this.increase = newValue - oldValue
        }
      }
    })
  </script>
</body>
</html>

```

### filter

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <p>{{ numbers | getOddNums | getUnderTenNums }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
      },
      filters: {
        getOddNums: function (nums) {
          const oddNums = nums.filter((num) => {
            return num % 2
          })
          return oddNums
        },
        getUnderTenNums: function (nums) {
          const underTen = nums.filter((num) => {
            return num < 10
          })
          return underTen
        }
      }
    })
  </script>
</body>
</html>

```

### v-if 와 v-for 혼용

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">
    <!-- bad 1 -->
    <ul>
      <li
        v-for="user in users"
        v-if="user.isActive"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>

    <!-- good 1 -->
    <ul>
      <li
        v-for="user in activeUsers"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>

    <!-- bad 2 -->
    <ul>
      <li
        v-for="user in users"
        v-if="shouldShowUsers"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>

    <!-- good 2 -->
    <ul v-if="shouldShowUsers">
      <li
        v-for="user in users"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        users: [
          { id: 1, name: 'harry', isActive: false, },
          { id: 2, name: 'john', isActive: true, },
          { id: 3, name: 'tony', isActive: false, },
          { id: 4, name: 'eric', isActive: true, },
        ],
        shouldShowUsers: true,
      },
      computed: {
        activeUsers: function () {
          return this.users.filter(user => {
            return user.isActive
          })
        }
      },
    })
  </script>
</body>
</html>

```

### lodash

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>  <script>
    console.log('-----------------1. reverse---------------')
    //1. reverse - Vanilla O
    // Vanilla
    const array1 = [1, 2, 3, 4]
    const reversedArray1 = array1.reverse()
    console.log(reversedArray1)

    // Lodash
    const array2 = [1, 2, 3, 4]
    const reversedArray2 = _.reverse(array2)
    console.log(reversedArray2) // [4, 3, 2, 1]


    console.log('-----------------2. sort---------------')
    //2. sort - Weird Operation in Vanilla 
    // Vanilla 
    const numbers1 = [10, 1, 3, 7, 4]
    // numbers1.sort()
    // console.log(numbers1)

    numbers1.sort(function (num1, num2) {
      return num1 - num2
    })
    console.log(numbers1)

    // Lodash
    const numbers2 = [10, 1, 3, 7, 4]
    const sortedNumbers2 = _.sortBy(numbers2)
    console.log(sortedNumbers2)


    console.log('-----------------3-1. range---------------')
    //3. range - Vanilla X
    // Lodash
    const nums1 = _.range(4)
    const nums2 = _.range(1, 5)
    const nums3 = _.range(1, 7, 2)

    console.log(nums1) // [0, 1, 2, 3]
    console.log(nums2) // [1, 2, 3, 4]
    console.log(nums3) // [1, 3, 5]

    console.log('-----------------3-2. random---------------')
    //3-2. random - Vanilla ?
    const randomNum1 = _.random(0, 5) // 0, 1, 2, 3, 4, 5
    const randomNum2 = _.random(5) // 1, 2, 3, 4, 5
    const randomNum3 = _.random(1.2, 5.2)

    console.log(randomNum1)
    console.log(randomNum2)
    console.log(randomNum3)
    

    console.log('-----------------3-3. sampleSize---------------')
    //3-3. sampleSize - Vanilla ?
    const result = _.sampleSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
    console.log(result)

    // 정렬까지
    const sortedResult = _.sortBy(result)
    console.log(sortedResult)

    console.log('-----------------4. Lotto---------------')
    const lottoNums = _.sampleSize(_.range(1, 46), 6)
    const sortedLottoNums = _.sortBy(lottoNums)
    console.log(sortedLottoNums)

  </script>
</body>
</html>

```





## 2. 통신 : 회원가입, 로그인, 로그아웃

