from enum import Enum

MALE = "male"
FEMALE = "female"
OTHER = "other"

GENDERS = ((MALE, MALE), (FEMALE, FEMALE), (OTHER, OTHER))

MEMBER = "member"
LEADER = "leader"
CO_LEADER = "co-leader"
TREASURER = "treasurer"
RECRUITING = "recruiting"
DEVELOPMENT = "development"
EDITOR = "editor"
RETIREE = "retiree"
MEDIA_RELATIONS = "media_relations"
ACTIVE_RETIREE = "active_retiree"
ALUMNI = "alumni"
WEBMASTER = "webmaster"
INTEREST_GROUP_ADMIN = "interest_group_admin"
ALUMNI_ADMIN = "alumni_admin"
RETIREE_EMAIL = "retiree_email"
COMPANY_ADMIN = "company_admin"
DUGNAD_ADMIN = "dugnad_admin"
TRIP_ADMIN = "trip_admin"
SPONSOR_ADMIN = "sponsor_admin"
SOCIAL_ADMIN = "social_admin"

ROLES = (
    (MEMBER, MEMBER),
    (LEADER, LEADER),
    (CO_LEADER, CO_LEADER),
    (TREASURER, TREASURER),
    (RECRUITING, RECRUITING),
    (DEVELOPMENT, DEVELOPMENT),
    (EDITOR, EDITOR),
    (RETIREE, RETIREE),
    (MEDIA_RELATIONS, MEDIA_RELATIONS),
    (ACTIVE_RETIREE, ACTIVE_RETIREE),
    (ALUMNI, ALUMNI),
    (WEBMASTER, WEBMASTER),
    (INTEREST_GROUP_ADMIN, INTEREST_GROUP_ADMIN),
    (ALUMNI_ADMIN, ALUMNI_ADMIN),
    (RETIREE_EMAIL, RETIREE_EMAIL),
    (COMPANY_ADMIN, COMPANY_ADMIN),
    (DUGNAD_ADMIN, DUGNAD_ADMIN),
    (TRIP_ADMIN, TRIP_ADMIN),
    (SPONSOR_ADMIN, SPONSOR_ADMIN),
    (SOCIAL_ADMIN, SOCIAL_ADMIN),
)

DATA = "data"
KOMTEK = "komtek"

COURSES = ((DATA, DATA), (KOMTEK, KOMTEK))

DATA_LONG = "Datateknologi"
KOMTEK_LONG = "Kommunikasjonsteknologi"

COURSES_LONG = ((DATA_LONG, DATA_LONG), (KOMTEK_LONG, KOMTEK_LONG))

FIRST_GRADE_DATA = "1. klasse Datateknologi"
FIRST_GRADE_KOMTEK = "1. klasse Kommunikasjonsteknologi"

FOURTH_GRADE_DATA = "4. klasse Datateknologi"
FOURTH_GRADE_KOMTEK = "4. klasse Kommunikasjonsteknologi"

FIRST_GRADES = (
    (FIRST_GRADE_DATA, FIRST_GRADE_DATA),
    (FIRST_GRADE_KOMTEK, FIRST_GRADE_KOMTEK),
)

USER_GROUP = "Users"
MEMBER_GROUP = "Abakus"


class FSGroup(Enum):
    @classmethod
    def values(cls) -> list[str]:
        return [e.value for e in cls]

    MTDT = "fc:fs:fs:prg:ntnu.no:mtdt"
    MTKOM = "fc:fs:fs:prg:ntnu.no:mtkom"
    MIDT = "fc:fs:fs:prg:ntnu.no:midt"
    MSTCNNS = "fc:fs:fs:prg:ntnu.no:mstcnns"


AbakusGradeFSMapping = {
    FSGroup.MTDT: FIRST_GRADE_DATA,
    FSGroup.MTKOM: FIRST_GRADE_KOMTEK,
    FSGroup.MIDT: FOURTH_GRADE_DATA,
    FSGroup.MSTCNNS: FOURTH_GRADE_KOMTEK,
}

STUDENT_EMAIL_DOMAIN = "stud.ntnu.no"

GROUP_COMMITTEE = "komite"
GROUP_INTEREST = "interesse"
GROUP_BOARD = "styre"
GROUP_REVUE = "revy"
GROUP_SUB = "under"
GROUP_GRADE = "klasse"
GROUP_OTHER = "annen"
GROUP_TYPES = (
    (GROUP_COMMITTEE, GROUP_COMMITTEE),
    (GROUP_INTEREST, GROUP_INTEREST),
    (GROUP_BOARD, GROUP_BOARD),
    (GROUP_REVUE, GROUP_REVUE),
    (GROUP_GRADE, GROUP_GRADE),
    (GROUP_OTHER, GROUP_OTHER),
    (GROUP_SUB, GROUP_SUB),
)
OPEN_GROUPS = (GROUP_INTEREST,)

PUBLIC_GROUPS = (GROUP_INTEREST, GROUP_COMMITTEE, GROUP_SUB, GROUP_BOARD, GROUP_REVUE)


SPRING = "spring"
AUTUMN = "autumn"

SEMESTERS = (
    (SPRING, SPRING),
    (AUTUMN, AUTUMN),
)

WEBSITE_DOMAIN = "WEBSITE"
SOCIAL_MEDIA_DOMAIN = "SOCIAL_MEDIA"
PHOTO_CONSENT_DOMAINS = (
    (WEBSITE_DOMAIN, WEBSITE_DOMAIN),
    (SOCIAL_MEDIA_DOMAIN, SOCIAL_MEDIA_DOMAIN),
)

AUTO_THEME = "auto"
LIGHT_THEME = "light"
DARK_THEME = "dark"

THEMES = (
    (AUTO_THEME, AUTO_THEME),
    (LIGHT_THEME, LIGHT_THEME),
    (DARK_THEME, DARK_THEME),
)
