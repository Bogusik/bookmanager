<template>
  <el-card style="width: 100%; max-width: 1024px; margin: 0 auto;" shadow="never">
   <el-table :data="fetchedBooks">
    <el-table-column type="expand">
      <template slot-scope="scope">
        <img :src="scope.row.poster_image" />
        <p>{{ scope.row.description }}</p>
      </template>
    </el-table-column>
    <el-table-column
      prop="title"
      label="Title">
    </el-table-column>
    <el-table-column
      prop="author"
      label="Author">
    </el-table-column>
    <el-table-column
      label="Operations">
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="primary" 
          icon="el-icon-edit"
          @click="handleEdit(scope.$index, scope.row)"
          circle />
        <el-button
          size="mini"
          type="danger"
          icon="el-icon-delete"
          @click="handleDelete(scope.$index, scope.row)"
          circle />
      </template>
    </el-table-column>
  </el-table>
  </el-card>

</template>

<script>

export default {
  name: 'BooksList',
  computed: {
    fetchedBooks () {
      return this.$store.state.books
    }
  },
  mounted () {
    this.$store.dispatch('getBooks')
  },
  methods: {
    handleDelete(index, row) {
      this.$store.dispatch('removeBook', row.id)
    },
    handleEdit(index, row) {
      this.$router.push(`/edit/${row.id}`)
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  img {
    max-width: 25%;
    max-height: 250px;
    margin: 10px;
  }
  p, img {
    float: left;
  } 
</style>