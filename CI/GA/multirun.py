#fitness[i] = self.fitness_f(generation[i])
                #mp that line
                core_num = 4
                batch_size = l/core_num
 
                #print 'creating missions'
                missions = zip(range(l), generation)
                def f(mission):
                    for ind, ele in mission:
                        res.put((ind, self.fitness_f(ele)))

                #print 'processing'
                tasks = []
                for ind in range(core_num):
                    if ind+1 == core_num:
                        p = mp.Process(target = f, name = 'MP:'+str(ind), args=(missions[ind * batch_size:],))
                    else:
                        p = mp.Process(target = f, name = 'MP:'+str(ind),
                                       args=(missions[ind * batch_size:(ind+1) * batch_size], ))
                    tasks.append(p)
                    p.start()

                for task in tasks:
                    task.join()

                #the context is copied by other processing
                #restore the context
                res.refresh()
                for ind in range(l):
                    index, value = res.get()
                    fitness[index] = value                    
                    if fitness_max == None or self.cmp_f(value, fitness_max):
                        fitness_max = value 
                        best_child = generation[index]


