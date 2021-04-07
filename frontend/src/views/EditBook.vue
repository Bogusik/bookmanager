<template>
  <div>
    <page-header :backTitle="book.title" />
    <el-row>
      <book-form :book="book" :submitForm="submitForm" />
    </el-row>
  </div>
</template>

<script>
import BookForm from '../components/BookForm.vue'
import PageHeader from '../components/PageHeader.vue'

export default {
  components: { PageHeader, BookForm },
  name: 'EditBook',
  computed: {
    book () {
      return this.$store.state.books.filter(book => book.id === parseInt(this.$route.params.id))[0]
    }
  },
  mounted () {
    this.$store.dispatch('getBooks')
  },
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
      await this.axios.patch(`/books/${this.$route.params.id}/`, data, conf)
      } catch(e) {
        console.log(e.response)
      }
      this.$store.dispatch('getBooks')
    }
  }
}
</script>