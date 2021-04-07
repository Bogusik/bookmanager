<template>
<el-form ref="form" label-position="left" label-width="100px">
  <el-form-item label="Username">
    <el-input v-model="formData.username" placeholder="myuser"></el-input>
  </el-form-item>
  <el-form-item label="Password">
    <el-input v-model="formData.password" show-password></el-input>
  </el-form-item>
  <el-form-item>
  <el-button type="primary" @click="tryLogin()">Login</el-button>
  </el-form-item>
</el-form>
</template>

<script>
import store from '../store';

export default {
  name: 'LoginForm',
  data() {
    return {
      formData: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    tryLogin () {
      store.dispatch('LogIn', this.formData)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
