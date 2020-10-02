var words=["GOOGLE","MICROSOFT","ADOBE","TWITTER","Honchous","AMAZON","SAMSUNG",
            "IBM","SNAPCHAT","ORACLE","FACEBOOK"];
const companies=new Vue({
  el:"#words",
  data:{
    words:words
  }
});
var letters=[ 'B','X','s','u','o','h','c','n','o','H','X','K',
              'O','B','Z','E','M','U','B','A','X','L','C','W',
              'J','Y','H','B','P','V','C','G','P','F','D','Y',
              'T','S','I','B','I','O','B','Z','A','P','Y','U',
              'F','A','J','O','Q','D','D','C','T','V','L','H',
              'O','M','N','J','O','J','E','O','A','T','N','E',
              'S','S','N','M','H','B','R','R','H','W','E','L',
              'O','U','R','O','O','E','N','A','C','I','B','T',
              'R','N','H','O','Z','T','Z','C','P','T','O','V',
              'C','G','K','W','F','A','Q','L','A','T','D','R',
              'I','H','L','R','S','I','M','E','N','E','A','O',
              'M','E','L','G','O','O','G','A','S','R','T','E'];

const letter=new Vue({
  el:"#boxOfLetters",
  data:{
    char:letters,
    num:0
  },
  methods:{
    identity: function(index){
      index=index+1;
      return "l"+index.toString();
    },
    highlight: function(event){
      if(event.target.className=="boxes")
      {
        if(event.target.style.backgroundColor=="tomato")
        {
          event.target.style.backgroundColor="mediumvioletred";
          check(event);
        }
        else
        {
          event.target.style.backgroundColor="tomato";
          check(event);
        }
      }
      if(event.target.parentNode.className=="boxes")
      {
        if(event.target.parentNode.style.backgroundColor=="tomato")
        {
          event.target.parentNode.style.backgroundColor="mediumvioletred";
          check(event);
        }
        else
        {
          event.target.parentNode.style.backgroundColor="tomato";
          check(event);
        }
      }
    }
  }
});

var ids=[];
for(let i=1;i<=letters.length;i++)
{
  var str="l"+i.toString();
  ids[i-1]=document.getElementById(str);
}

var list={
   GOOGLE : [ids[133].id,ids[134].id,ids[135].id,ids[136].id,ids[137].id,ids[138].id],
   MICROSOFT : [ids[132].id,ids[120].id,ids[108].id,ids[96].id,ids[84].id,ids[72].id,ids[60].id,ids[48].id,ids[36].id],
   ADOBE :  [ids[130].id,ids[118].id,ids[106].id,ids[94].id,ids[82].id],
   TWITTER : [ids[69].id,ids[81].id,ids[93].id,ids[105].id,ids[117].id,ids[129].id,ids[141].id],
  Honchous : [ids[2].id,ids[3].id,ids[4].id,ids[5].id,ids[6].id,ids[7].id,ids[8].id,ids[9].id],
   AMAZON : [ids[139].id,ids[126].id,ids[113].id,ids[100].id,ids[87].id,ids[74].id],
   SAMSUNG : [ids[37].id,ids[49].id,ids[61].id,ids[73].id,ids[85].id,ids[97].id,ids[109].id],
   IBM : [ids[38].id,ids[27].id,ids[16].id],
   APPLE :[ids[19].id,ids[32].id,ids[45].id,ids[58].id,ids[71].id],
   SNAPCHAT :[ids[140].id,ids[128].id,ids[116].id,ids[104].id,ids[92].id,ids[80].id,ids[68].id,ids[56].id],
   ORACLE :[ids[67].id,ids[79].id,ids[91].id,ids[103].id,ids[115].id,ids[127].id],
   FACEBOOK :[ids[33].id,ids[44].id,ids[55].id,ids[66].id,ids[77].id,ids[88].id,ids[99].id,ids[110].id]
};

function check(event){
  for(var comp in list)
  {
    if(list[comp].includes(event.target.id.toString() || event.target.firstElementChild.id.toString()))
    {
      var con=true;
      for(let i=0;i<list[comp].length;i++)
        {
          if(document.getElementById(list[comp][i]).parentNode.style.backgroundColor!="mediumvioletred")
          {
            con=false;
            break;
          }
        }
         if(con==true)
        {
          for(let i=0;i<list[comp].length;i++)
          {
            document.getElementById(list[comp][i]).parentNode.style.backgroundColor="#3cc33c";
            document.getElementById(list[comp][i]).style.color="black";
            document.getElementById(list[comp][i]).parentNode.style.pointerEvents='none';
          }
          document.querySelector("."+comp).style.color="#3cc33c";
          
          points.correct+=1;
        }
    }
  }
}

var points=new Vue({
  el:"#points",
  data:{
    correct:0
  }
})