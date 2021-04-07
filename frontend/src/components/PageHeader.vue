<template>
    <el-row style="width: 100%; max-width: 1024px; margin: 0 auto;">
      <el-col :span="24" style="padding: 10px 20px;">
        <el-page-header v-if="backTitle" @back="goBack" :content="backTitle" style="float: left;"></el-page-header>
        <el-button v-else type="success" @click="addBookPage" icon="el-icon-plus" circle></el-button>
        <el-dropdown @command="handleCommand" style="float: right;">
          <span class="el-dropdown-link">
            <h4><span style="color: #409EFF">{{ fetchedUser.username }}</span><i class="el-icon-arrow-down el-icon--right"></i></h4>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="LogOut">Log Out</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-col>
    </el-row>
</template>

<script>
import router from '../router'

export default {
  name: 'PageHeader',
  props: {
    backTitle: {
      type: String,
      default: ""
    }
  },
  computed: {
    fetchedUser () {
      return this.$store.state.user
    }
  },
  methods: {
    handleCommand(arg) {
      if (arg === 'LogOut') {
        this.LogOut()
      }
    },
    LogOut () {
      localStorage.removeItem('token')
      router.push('/login')
    },
    goBack() {
      router.push({name: 'Books'})
    },
    addBookPage() {
      router.push({name: 'AddBook'})
    }
  }
}
</script>