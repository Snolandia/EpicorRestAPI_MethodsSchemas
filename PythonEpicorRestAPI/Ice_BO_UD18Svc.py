import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.UD18Svc
# Description: User Defined Table 18
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_UD18s(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UD18s items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UD18s
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD18Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18s",headers=creds) as resp:
           return await resp.json()

async def post_UD18s(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UD18s
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UD18Row
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UD18Row
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18s", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UD18s_Company_Key1_Key2_Key3_Key4_Key5(Company, Key1, Key2, Key3, Key4, Key5, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD18 item
   Description: Calls GetByID to retrieve the UD18 item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD18
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD18Row
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UD18s_Company_Key1_Key2_Key3_Key4_Key5(Company, Key1, Key2, Key3, Key4, Key5, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UD18 for the service
   Description: Calls UpdateExt to update UD18. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UD18
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UD18Row
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UD18s_Company_Key1_Key2_Key3_Key4_Key5(Company, Key1, Key2, Key3, Key4, Key5, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UD18 item
   Description: Call UpdateExt to delete UD18 item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UD18
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")",headers=creds) as resp:
           return await resp.json()

async def get_UD18s_Company_Key1_Key2_Key3_Key4_Key5_UD18Attchs(Company, Key1, Key2, Key3, Key4, Key5, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get UD18Attchs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_UD18Attchs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD18AttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/UD18Attchs",headers=creds) as resp:
           return await resp.json()

async def get_UD18s_Company_Key1_Key2_Key3_Key4_Key5_UD18Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD18Attch item
   Description: Calls GetByID to retrieve the UD18Attch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD18Attch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD18AttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18s(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + ")/UD18Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_UD18Attchs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UD18Attchs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UD18Attchs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD18AttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18Attchs",headers=creds) as resp:
           return await resp.json()

async def post_UD18Attchs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UD18Attchs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.UD18AttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.UD18AttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18Attchs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UD18Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UD18Attch item
   Description: Calls GetByID to retrieve the UD18Attch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UD18Attch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.UD18AttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UD18Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UD18Attch for the service
   Description: Calls UpdateExt to update UD18Attch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UD18Attch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.UD18AttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UD18Attchs_Company_Key1_Key2_Key3_Key4_Key5_DrawingSeq(Company, Key1, Key2, Key3, Key4, Key5, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UD18Attch item
   Description: Call UpdateExt to delete UD18Attch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UD18Attch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/UD18Attchs(" + Company + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.UD18ListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseUD18, whereClauseUD18Attch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUD18=" + whereClauseUD18
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUD18Attch=" + whereClauseUD18Attch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(key1, key2, key3, key4, key5, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key4=" + key4
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key5=" + key5

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetaNewUD18(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetaNewUD18
   Description: Get new for UD18.
   OperationID: GetaNewUD18
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetaNewUD18_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetaNewUD18_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUD18(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUD18
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUD18
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUD18_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUD18_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUD18Attch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUD18Attch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUD18Attch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUD18Attch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUD18Attch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.UD18Svc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD18AttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UD18AttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD18ListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UD18ListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_UD18Row:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_UD18Row] = obj["value"]
      pass

class Ice_Tablesets_UD18AttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD18ListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.ShortChar11:str = obj["ShortChar11"]
      """  ShortChar11  """  
      self.ShortChar12:str = obj["ShortChar12"]
      """  ShortChar12  """  
      self.ShortChar13:str = obj["ShortChar13"]
      """  ShortChar13  """  
      self.ShortChar14:str = obj["ShortChar14"]
      """  ShortChar14  """  
      self.ShortChar15:str = obj["ShortChar15"]
      """  ShortChar15  """  
      self.ShortChar16:str = obj["ShortChar16"]
      """  ShortChar16  """  
      self.ShortChar17:str = obj["ShortChar17"]
      """  ShortChar17  """  
      self.ShortChar18:str = obj["ShortChar18"]
      """  ShortChar18  """  
      self.ShortChar19:str = obj["ShortChar19"]
      """  ShortChar19  """  
      self.ShortChar20:str = obj["ShortChar20"]
      """  ShortChar20  """  
      self.GlobalUD18:bool = obj["GlobalUD18"]
      """  GlobalUD18  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD18Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.ShortChar11:str = obj["ShortChar11"]
      """  ShortChar11  """  
      self.ShortChar12:str = obj["ShortChar12"]
      """  ShortChar12  """  
      self.ShortChar13:str = obj["ShortChar13"]
      """  ShortChar13  """  
      self.ShortChar14:str = obj["ShortChar14"]
      """  ShortChar14  """  
      self.ShortChar15:str = obj["ShortChar15"]
      """  ShortChar15  """  
      self.ShortChar16:str = obj["ShortChar16"]
      """  ShortChar16  """  
      self.ShortChar17:str = obj["ShortChar17"]
      """  ShortChar17  """  
      self.ShortChar18:str = obj["ShortChar18"]
      """  ShortChar18  """  
      self.ShortChar19:str = obj["ShortChar19"]
      """  ShortChar19  """  
      self.ShortChar20:str = obj["ShortChar20"]
      """  ShortChar20  """  
      self.GlobalUD18:bool = obj["GlobalUD18"]
      """  GlobalUD18  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UD18Tableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UD18Tableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UD18Tableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UD18ListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewUD18Attch_input:
   """ Required : 
   ds
   key1
   key2
   key3
   key4
   key5
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD18Tableset] = obj["ds"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      pass

class GetNewUD18Attch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD18Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUD18_input:
   """ Required : 
   ds
   key1
   key2
   key3
   key4
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD18Tableset] = obj["ds"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      pass

class GetNewUD18_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD18Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseUD18
   whereClauseUD18Attch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseUD18:str = obj["whereClauseUD18"]
      self.whereClauseUD18Attch:str = obj["whereClauseUD18Attch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_UD18Tableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetaNewUD18_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD18Tableset] = obj["ds"]
      pass

class GetaNewUD18_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD18Tableset] = obj["ds"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class Ice_Tablesets_UD18AttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD18ListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.ShortChar11:str = obj["ShortChar11"]
      """  ShortChar11  """  
      self.ShortChar12:str = obj["ShortChar12"]
      """  ShortChar12  """  
      self.ShortChar13:str = obj["ShortChar13"]
      """  ShortChar13  """  
      self.ShortChar14:str = obj["ShortChar14"]
      """  ShortChar14  """  
      self.ShortChar15:str = obj["ShortChar15"]
      """  ShortChar15  """  
      self.ShortChar16:str = obj["ShortChar16"]
      """  ShortChar16  """  
      self.ShortChar17:str = obj["ShortChar17"]
      """  ShortChar17  """  
      self.ShortChar18:str = obj["ShortChar18"]
      """  ShortChar18  """  
      self.ShortChar19:str = obj["ShortChar19"]
      """  ShortChar19  """  
      self.ShortChar20:str = obj["ShortChar20"]
      """  ShortChar20  """  
      self.GlobalUD18:bool = obj["GlobalUD18"]
      """  GlobalUD18  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD18ListTableset:
   def __init__(self, obj):
      self.UD18List:list[Ice_Tablesets_UD18ListRow] = obj["UD18List"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UD18Row:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Key1:str = obj["Key1"]
      """  Key1  """  
      self.Key2:str = obj["Key2"]
      """  Key2  """  
      self.Key3:str = obj["Key3"]
      """  Key3  """  
      self.Key4:str = obj["Key4"]
      """  Key4  """  
      self.Key5:str = obj["Key5"]
      """  Key5  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      """  Character02  """  
      self.Character03:str = obj["Character03"]
      """  Character03  """  
      self.Character04:str = obj["Character04"]
      """  Character04  """  
      self.Character05:str = obj["Character05"]
      """  Character05  """  
      self.Character06:str = obj["Character06"]
      """  Character06  """  
      self.Character07:str = obj["Character07"]
      """  Character07  """  
      self.Character08:str = obj["Character08"]
      """  Character08  """  
      self.Character09:str = obj["Character09"]
      """  Character09  """  
      self.Character10:str = obj["Character10"]
      """  Character10  """  
      self.Number01:int = obj["Number01"]
      """  Number01  """  
      self.Number02:int = obj["Number02"]
      """  Number02  """  
      self.Number03:int = obj["Number03"]
      """  Number03  """  
      self.Number04:int = obj["Number04"]
      """  Number04  """  
      self.Number05:int = obj["Number05"]
      """  Number05  """  
      self.Number06:int = obj["Number06"]
      """  Number06  """  
      self.Number07:int = obj["Number07"]
      """  Number07  """  
      self.Number08:int = obj["Number08"]
      """  Number08  """  
      self.Number09:int = obj["Number09"]
      """  Number09  """  
      self.Number10:int = obj["Number10"]
      """  Number10  """  
      self.Number11:int = obj["Number11"]
      """  Number11  """  
      self.Number12:int = obj["Number12"]
      """  Number12  """  
      self.Number13:int = obj["Number13"]
      """  Number13  """  
      self.Number14:int = obj["Number14"]
      """  Number14  """  
      self.Number15:int = obj["Number15"]
      """  Number15  """  
      self.Number16:int = obj["Number16"]
      """  Number16  """  
      self.Number17:int = obj["Number17"]
      """  Number17  """  
      self.Number18:int = obj["Number18"]
      """  Number18  """  
      self.Number19:int = obj["Number19"]
      """  Number19  """  
      self.Number20:int = obj["Number20"]
      """  Number20  """  
      self.Date01:str = obj["Date01"]
      """  Date01  """  
      self.Date02:str = obj["Date02"]
      """  Date02  """  
      self.Date03:str = obj["Date03"]
      """  Date03  """  
      self.Date04:str = obj["Date04"]
      """  Date04  """  
      self.Date05:str = obj["Date05"]
      """  Date05  """  
      self.Date06:str = obj["Date06"]
      """  Date06  """  
      self.Date07:str = obj["Date07"]
      """  Date07  """  
      self.Date08:str = obj["Date08"]
      """  Date08  """  
      self.Date09:str = obj["Date09"]
      """  Date09  """  
      self.Date10:str = obj["Date10"]
      """  Date10  """  
      self.Date11:str = obj["Date11"]
      """  Date11  """  
      self.Date12:str = obj["Date12"]
      """  Date12  """  
      self.Date13:str = obj["Date13"]
      """  Date13  """  
      self.Date14:str = obj["Date14"]
      """  Date14  """  
      self.Date15:str = obj["Date15"]
      """  Date15  """  
      self.Date16:str = obj["Date16"]
      """  Date16  """  
      self.Date17:str = obj["Date17"]
      """  Date17  """  
      self.Date18:str = obj["Date18"]
      """  Date18  """  
      self.Date19:str = obj["Date19"]
      """  Date19  """  
      self.Date20:str = obj["Date20"]
      """  Date20  """  
      self.CheckBox01:bool = obj["CheckBox01"]
      """  CheckBox01  """  
      self.CheckBox02:bool = obj["CheckBox02"]
      """  CheckBox02  """  
      self.CheckBox03:bool = obj["CheckBox03"]
      """  CheckBox03  """  
      self.CheckBox04:bool = obj["CheckBox04"]
      """  CheckBox04  """  
      self.CheckBox05:bool = obj["CheckBox05"]
      """  CheckBox05  """  
      self.CheckBox06:bool = obj["CheckBox06"]
      """  CheckBox06  """  
      self.CheckBox07:bool = obj["CheckBox07"]
      """  CheckBox07  """  
      self.CheckBox08:bool = obj["CheckBox08"]
      """  CheckBox08  """  
      self.CheckBox09:bool = obj["CheckBox09"]
      """  CheckBox09  """  
      self.CheckBox10:bool = obj["CheckBox10"]
      """  CheckBox10  """  
      self.CheckBox11:bool = obj["CheckBox11"]
      """  CheckBox11  """  
      self.CheckBox12:bool = obj["CheckBox12"]
      """  CheckBox12  """  
      self.CheckBox13:bool = obj["CheckBox13"]
      """  CheckBox13  """  
      self.CheckBox14:bool = obj["CheckBox14"]
      """  CheckBox14  """  
      self.CheckBox15:bool = obj["CheckBox15"]
      """  CheckBox15  """  
      self.CheckBox16:bool = obj["CheckBox16"]
      """  CheckBox16  """  
      self.CheckBox17:bool = obj["CheckBox17"]
      """  CheckBox17  """  
      self.CheckBox18:bool = obj["CheckBox18"]
      """  CheckBox18  """  
      self.CheckBox19:bool = obj["CheckBox19"]
      """  CheckBox19  """  
      self.CheckBox20:bool = obj["CheckBox20"]
      """  CheckBox20  """  
      self.ShortChar01:str = obj["ShortChar01"]
      """  ShortChar01  """  
      self.ShortChar02:str = obj["ShortChar02"]
      """  ShortChar02  """  
      self.ShortChar03:str = obj["ShortChar03"]
      """  ShortChar03  """  
      self.ShortChar04:str = obj["ShortChar04"]
      """  ShortChar04  """  
      self.ShortChar05:str = obj["ShortChar05"]
      """  ShortChar05  """  
      self.ShortChar06:str = obj["ShortChar06"]
      """  ShortChar06  """  
      self.ShortChar07:str = obj["ShortChar07"]
      """  ShortChar07  """  
      self.ShortChar08:str = obj["ShortChar08"]
      """  ShortChar08  """  
      self.ShortChar09:str = obj["ShortChar09"]
      """  ShortChar09  """  
      self.ShortChar10:str = obj["ShortChar10"]
      """  ShortChar10  """  
      self.ShortChar11:str = obj["ShortChar11"]
      """  ShortChar11  """  
      self.ShortChar12:str = obj["ShortChar12"]
      """  ShortChar12  """  
      self.ShortChar13:str = obj["ShortChar13"]
      """  ShortChar13  """  
      self.ShortChar14:str = obj["ShortChar14"]
      """  ShortChar14  """  
      self.ShortChar15:str = obj["ShortChar15"]
      """  ShortChar15  """  
      self.ShortChar16:str = obj["ShortChar16"]
      """  ShortChar16  """  
      self.ShortChar17:str = obj["ShortChar17"]
      """  ShortChar17  """  
      self.ShortChar18:str = obj["ShortChar18"]
      """  ShortChar18  """  
      self.ShortChar19:str = obj["ShortChar19"]
      """  ShortChar19  """  
      self.ShortChar20:str = obj["ShortChar20"]
      """  ShortChar20  """  
      self.GlobalUD18:bool = obj["GlobalUD18"]
      """  GlobalUD18  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  GlobalLock  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UD18Tableset:
   def __init__(self, obj):
      self.UD18:list[Ice_Tablesets_UD18Row] = obj["UD18"]
      self.UD18Attch:list[Ice_Tablesets_UD18AttchRow] = obj["UD18Attch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtUD18Tableset:
   def __init__(self, obj):
      self.UD18:list[Ice_Tablesets_UD18Row] = obj["UD18"]
      self.UD18Attch:list[Ice_Tablesets_UD18AttchRow] = obj["UD18Attch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtUD18Tableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtUD18Tableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UD18Tableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UD18Tableset] = obj["ds"]
      pass

      """  output parameters  """  

