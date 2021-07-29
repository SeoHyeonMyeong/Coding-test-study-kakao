/*
 * 신규 아이디 추천
 * https://programmers.co.kr/learn/courses/30/lessons/72410
 */

fun isNumeric(char: Char) = char in '0'..'9'

fun main() {
    var id:String = "aaasssddd..YOuR_3*-아.id.이.디.."
    println(id)

    // 1단계 id의 모든 대문자를 소문자로 치환합니다.
    var new_id = id.toMutableList()
    for(i in new_id.indices){
        if (new_id[i].isUpperCase()){
            new_id.set(i,new_id[i].toLowerCase())
        }
    }
    println(new_id)
    
    id = new_id.toString()
	println(id)

    // 2단계 id에서 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거합니다.
    var temp:String = ""
    for(i in new_id.indices){
        val condition1 = new_id[i].isLowerCase()
        val condition2 = isNumeric(new_id[i])
        val condition3 = new_id[i]=='-'
        val condition4 = new_id[i]=='_'
        val condition5 = new_id[i]=='.'
        if (condition1 || condition2 || condition3 || condition4 || condition5){
            temp = temp + new_id[i]
        }
    }
    println(temp)

    // 3단계 id에서 마침표가 2번이상 반복되면 한개로 치환합니다.
    new_id = temp.toMutableList()
    temp = ""
    for(i in new_id.indices){
        if (i == 0){
            temp = temp + new_id[i]
        }
        else if (new_id[i-1] == '.' && new_id[i] == '.'){
            
        }
        else{
            temp = temp + new_id[i]
        }
    }
    println(temp)

    // 4단계 id에서 마침표가 처음이나 끝에 위차한다면 제거합니다.
    new_id = temp.toMutableList()
    temp = ""
    for(i in new_id.indices){
        if(i == 0 || i == new_id.lastIndex){
            if(new_id[i]=='.'){

            }
            else{
                temp = temp + new_id[i]
            }
        }
        else{
            temp = temp + new_id[i]
        }
    }
    println(temp)

    // 5단계 id가 빈 문자열이면 a를 대입합니다.
    if (temp == ""){
        temp = "a"
    }

    // 6단계 id가 16자 이상이라면 첫 15개 문자를 제외한 나머지 문자를 모두 제거합니다.
    // 제거후 마침표가 id 끝에 위치한다면 마침표를 제거합니다.
    
    if (temp.length>15){
        temp = temp.substring(0,15)
        if (temp[14]=='.'){
            temp = temp.substring(0,14)
        }
    }
    println(temp)

    // 7단계 id의 길이가 2자 이하라면, id의 마지막 문자를 길이가 3이 될 때까지 반복해서 붙입니다.
    new_id = temp.toMutableList()
    while(temp.length<3){
        temp = temp + new_id[new_id.lastIndex]
    }
    println(temp)
}