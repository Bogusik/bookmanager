<template>
<el-tabs type="border-card" class="login-form" shadow="never">
  <el-tab-pane label="Sign in">
    <login-form></login-form>
  </el-tab-pane>
  <el-tab-pane label="Sign up">
    <registration-form></registration-form>
  </el-tab-pane>
</el-tabs>
</template>

<script>
// @ is an alias to /src
import LoginForm from '@/components/LoginForm.vue'
import RegistrationForm from '@/components/RegistrationForm.vue'

export default {
  name: 'Home',
  components: {
    LoginForm,
    RegistrationForm
  }
}
</script>

<style scoped>
.login-form {
  width: 100%;
  max-width: 600px; 
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
}
</style>