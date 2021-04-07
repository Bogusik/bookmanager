<template>
<el-card style="width: 100%; max-width: 1024px; margin: 0 auto;" shadow="never">
  <el-form v-if="book" label-position="left" label-width="100px">
    <el-form-item label="Title">
      <el-input v-model="book.title"></el-input>
    </el-form-item>
    <el-form-item label="Author">
      <el-input v-model="book.author"></el-input>
    </el-form-item>
    <el-form-item label="Description">
      <el-input v-model="book.description" type="textarea" rows="4" maxlength="500" show-word-limit></el-input>
    </el-form-item>
    <el-form-item label="Book cover">
      <el-upload
        class="upload-demo"
        action=""
        :on-change="getFile"
        :on-before-remove="removeFile"
        :limit="1"
        :auto-upload="false"
        :file-list="fileList"
        >
        <el-button size="small" type="primary">Click to upload a new one</el-button>
        <div slot="tip" class="el-upload__tip">jpg/png files</div>
      </el-upload>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm(asFormData)">Submit</el-button>
  </el-form-item>
  </el-form>
</el-card>
</template>

<script>

export default {
  name: 'BookForm',
  props: {
    book: {
      type: Object,
      default() { 
        return {
          title: "",
          author: "",
          description: "",
          poster_image: Object,
          id: ""
        }
      }
    },
    submitForm: Function
  },
  computed: {
    asFormData() {
      let data = this.book
      if (typeof data.poster_image === 'string') {
        delete data.poster_image
      } else {
        data.poster_image = data.poster_image.raw
      }
      const formData = new FormData()
      for(const [key, value] of Object.entries(data)) {
        formData.append(key, value)
      }
      return formData
    }
  },
  data() {
    return {
      fileList: [],
    };
  },
  methods: {
    getFile(file) {
      this.book.poster_image = file
    },
    removeFile() {
      delete this.book.poster_image
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-upload {
    margin: 0 auto;
  }
  .avatar-uploader {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
