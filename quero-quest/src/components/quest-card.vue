<template>
  <vk-card>
    <div class="body">
      <div class="title">
        <h3>placeholder problem title</h3>
      </div>
      <div class="votes small-text">
      <img src="@/assets/upvote.png" />
      </div>
      <div class="votes small-text">
      <img src="@/assets/questing.png" />
      </div>
      <div class="votes small-text">
      <img src="@/assets/downvote.png" />
      </div>
      <div class="desc small-text">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Suscipit eos neque non facilis tempora reprehenderit harum animi sint necessitatibus minima? Cum tenetur veniam harum porro maiores exercitationem accusantium, praesentium magnam commodi, cupiditate ducimus asperiores adipisci. Aliquid, repellat repudiandae voluptatem eos dolore cumque quas nostrum, perferendis doloremque, aliquam accusantium placeat eaque?</p>
      </div>	
    </div>
  </vk-card>
</template>


<script>
export default {
  name: "QuestCard",
}
</script>


<style scoped>
.body {
  display: grid;
  grid-template:
    "title desc" 1fr
    "votes desc" 1fr
    / 1fr 2fr;
}
.body .title {
  grid-area: title;

}
.body .title > * { 
	font-size: 1.3rem;
  font-weight: bold;
}
.small-text {
  font-size: 0.95rem;
}
.body .votes {
  grid-area: votes;
}
.body .desc {
  grid-area: desc;
}
#votes2{
  padding-left: 10%;
  padding-bottom: 0.5%;
  font-size: 95%;
}
#votes3{
  padding-left: 15%;
  padding-bottom: 0.5%;
  font-size: 95%;
}
</style>
