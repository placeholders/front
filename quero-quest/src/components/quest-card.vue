<template>
  <vk-card>
    <div class="body">
      <div class="title">
        <h3>placeholder problem title</h3>
      </div>
      <div class="votes">
      <img src="@/assets/upvote.png" />
      20
      </div>
      <div class="votes" id="voted">
      <img src="@/assets/questing.png"  />
      30
      </div>
      <div class="votes" id="votet">
      <img src="@/assets/downvote.png" />
      ph
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
    / 1fr 2fr
    

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
.body .votes2 {
  grid-area: votes2;
}
.body .votes3 {
  grid-area: votes3;
}
.body .desc {
  grid-area: desc;
}
#voted{
  padding-left: 32.5%;
}
#votet{
  padding-left: 65%;
}
</style>
