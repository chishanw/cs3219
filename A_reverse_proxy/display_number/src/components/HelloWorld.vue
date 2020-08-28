<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div>
    The number I've randomly generated is: {{ number }}!
    {{ my_message }}
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      number: 0,
      my_message: 'Hmm, a zero, how normal.'
    };
  },
  async mounted() {
    await axios({ method: "GET", "url": "http://localhost/number" })
        .then(result => {
          this.number = result.data['number'];
        }, error => {
          console.error(error);
        });
    await axios({ method: "GET", "url": `http://localhost/message?num=${this.number}` })
        .then(result => {
          this.my_message = result.data['message'];
        }, error => {
          console.error(error);
        });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
