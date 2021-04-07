<template>
  <div>
    <page-header></page-header>
    <el-row>
      <el-col :span="24">
        <books-list></books-list>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import BooksList from '../components/BooksList.vue'
import PageHeader from '../components/PageHeader.vue'

export default {
  components: { BooksList, PageHeader },
  name: 'Books'
}
</script>