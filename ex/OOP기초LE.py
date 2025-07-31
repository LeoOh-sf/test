# class 라는 것을 왜 쓸까?
# - 중복된 코드를 많이 줄일 수 있다

# 전사, 궁수, 마법사
# - 공통: 체력, 마나, 공격력
# - 기능: 공격하기, 걷기, 상태확인
# 전사만 할 수 있는 것: 칼로때리기(), 강하게소리지르기()
# 궁수만 할 수 있는 것: 활쏘기(), 자세히살펴보기()
# 마법사만 할 수 있는 것: 마법쓰기(), 똑똑해지기()

# 상황1. 전체 캐릭터의 수를 관리해야 한다
# - 전역변수로 관리
#  -> Character class 와 관련된 변수인데, 외부에 값을 관리
#  --> 유지보수가 어려워진다.

class Character:
    total_players = 0  # 클래스 변수
                       # 모든 인스턴스가 공유하는 값
    double_event = True  # ex) 경험치 2배 이벤트

    # self : 인스턴스 자기자신을 가리킨다
    # 생성자에 전달되는 값 : 인스턴스의 초기값
    def __init__(self, hp, mp, power, name):
        self.hp = hp
        self.mp = mp
        self.power = power
        self.name = name
        # 인스턴스 메서드에서 클래스 변수에 접근
        # Character.total_players += 1

    @classmethod
    def increment_player_count(cls):
        cls.total_players += 1

    # 인스턴스 메서드
    def attack(self):
        print(f"{self.power}의 데미지로 공격!")
    # 
    def walking(self):
        print(f'{self.name}이(가) 앞으로 걸어감')
    
    def status(self):
        print('stat_Info')
        print(f'Name: {self.name}')
        print(f'HP: {self.hp}')
        print(f'MP: {self.mp}')
        print(f'power: {self.power}')

    # 클래스 변수와 상관이 없고 인스턴스도 무관함
    # Character 클래스안에 있으면 좋을 것 같은 메서드
    # 20% 확률로 강하게 공격하는 치명타
    # class 안에 있으면 좋지만 밖에 나가야 하는것
    @staticmethod
    def critical_hit(power):
        import random
        if random.random() < 0.2:
            print("Critical Hit")
            return power*2
        return power
# 클래스명() => 클래스의 생성자를 호출해라고 정해놓음

character1 = Character(100, 50, 10, 'gg') # 1번 캐릭터 (인스턴스)
character2 = Character(500, 200, 100, 'faker')  # 2번 캐릭터 (인스턴스)

# character1.attack()
# character2.attack()
# character1.walking()
# character2.walking()
# character1.status()
# character2.status()


# # 인스턴스를 통해서도 클래스 변수에 접근 가능!
# # --> 하지마라!
# # print(f'전체 캐릭터 수 = {character1.total_players}')
# print(f'전체 캐릭터 수 = {Character.total_players}')

# # 내일 배울 것: 상속
# class Warrior(Character):
#     def 강하게때리기(self):
#         pass

#     def 소리지르기(self):
#         pass

# warrior1 = Warrior(200, 300, 50)
# print(warrior1.hp, warrior1.mp)

# class Archer:
#     pass

# class Wizard:
#     pass

# 내일 실습 할 것 : 인스턴스 메서드 추가해보기, 클래스 메서드, 스태틱 메서드
# - 상속 실습

# 전사만 할 수 있는 것: 칼로때리기(), 강하게소리지르기()
# 궁수만 할 수 있는 것: 활쏘기(), 자세히살펴보기()
# 마법사만 할 수 있는 것: 마법쓰기(), 똑똑해지기()
# - character class 안의 모든 속성 메서드는 포함하고
# + 본인 직업에 알맞는 기능들을 추가로 가짐

class Warrior(Character):
    total_players = 0
    # 생성자도 재정의가 된다네용 신기하네
    def __init__(self, hp, mp, power, name):
        # self.hp = hp + 100
        # self.mp = mp
        # self.power = power
        # self.name = name
        super().__init__(hp+100, mp, power, name)
    def slash(self):
        print(f'{self.name}이(가) slash를 사용했다')
    
    def cry(self):
        print(f'{self.name}이(가) cry를 사용했다')

    def attack(self): # 같은 함수 이름을 다시 재정의 하는 오버 라이딩
        print(f'{self.name}가 검으로 {self.power}의 데미지로 공격')

    @classmethod
    def increment_player_count(cls):
        cls.total_players += 1

warrior = Warrior(100, 50, 10, 'leo')
warrior.status()
warrior.attack()

print(f'전체 유저수 = {Warrior.total_players}')
# warrior hp +100/ archer power +50/ wizard mp +100

## 다중 상속

class Operator:
    def __init__(self):
        self.permission_level = '운영자'

    def ejection(self, target):
        print(f'{target}을 강퇴한다')

# operator class 및 warrior class 기능이 모두 포함된 클래스
class OperatorWarrior(Warrior, Operator):
    def __init__(self, hp, mp, power, name):
        Warrior.__init__(self, hp, mp, power, name)
        Operator.__init__(self)
# MRO 순서에 따라 자동 호출 -> 다중 상속 시에는 예기치 않은 클래스 호출 가능
print(OperatorWarrior.mro())
oper1 = OperatorWarrior(100, 100, 100, 'leo')
print(oper1.permission_level)
print(oper1.hp)

# 다중 상속 시, 슈퍼를 쓰려면 꽤나 치밀한 설계를 요구함
# 되도록 super 보다는 직접 명시를 사용하게 됨

## 상속 받아야하는 클래스가 입력 받는 입력 파라미터 숫자가 차이나면 못 쓴다
