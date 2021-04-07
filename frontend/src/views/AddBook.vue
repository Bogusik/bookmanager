<template>
  <div>
    <page-header backTitle="Add a book" />
    <el-row>
      <book-form :submitForm="submitForm" />
    </el-row>
  </div>
</template>

<script>
import BookForm from '../components/BookForm.vue'
import PageHeader from '../components/PageHeader.vue'

export default {
  components: { PageHeader, BookForm },
  name: 'EditBook',
  methods: {
    async submitForm(data) {
      const conf = { 
        headers: { 
          'Accept': 'application/json',
          'Content-Type': 'multipart/form-data',
          Authorization: "JWT " + localStorage.getItem('token') 
        }
      }
      try {
      await this.axios.post(`/books/`, data, conf)
      } catch(e) {
        console.log(e.response)
      }
      this.$store.dispatch('getBooks')
    }
  }
}
</script>