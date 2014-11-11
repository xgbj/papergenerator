drop table if exists paper;
create table paper (
  alias text not null,
  papername text not null,
  type integer not null,
  content text not null,
  optiona text not null,
  optionb text not null,
  optionc text not null,
  optiond text not null,
  answer text not null
);