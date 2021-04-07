<template>
<el-form label-position="left" label-width="100px">
  <el-form-item label="Username">
    <el-input v-model="formData.username" placeholder="myusername"></el-input>
  </el-form-item>
  <el-form-item label="First name">
    <el-input v-model="formData.first_name" placeholder="John"></el-input>
  </el-form-item>
  <el-form-item label="Last name">
    <el-input v-model="formData.last_name" placeholder="Johnson"></el-input>
  </el-form-item>
  <el-form-item label="Password">
    <el-input v-model="formData.password" show-password></el-input>
  </el-form-item>
  <el-form-item label="Email">
    <el-input v-model="formData.email" placeholder="mail@mail.com"></el-input>
  </el-form-item>
  <el-form-item>
  <el-button type="primary" @click="trySignUp()">Register</el-button>
  </el-form-item>
</el-form>
</template>

<script>
import store from '../store';

export default {
  name: 'RegistrationForm',
  data() {
    return {
      formData: {
        username: '',
        password: '',
        first_name: '',
        last_name: '',
      }
    }
  },
  methods: {
    async trySignUp () {
      await this.axios.post('/users/', this.formData)
      store.dispatch('LogIn', { username: this.formData.username, password: this.formData.password })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
