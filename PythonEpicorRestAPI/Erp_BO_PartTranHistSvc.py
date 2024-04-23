import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartTranHistSvc
# Description: Part Tracker Transaction History Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartTranHists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartTranHists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartTranHists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists",headers=creds) as resp:
           return await resp.json()

async def post_PartTranHists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartTranHists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartTranHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartTranHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartTranHists_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartTranHist item
   Description: Calls GetByID to retrieve the PartTranHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartTranHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartTranHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartTranHists_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartTranHist for the service
   Description: Calls UpdateExt to update PartTranHist. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartTranHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartTranHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartTranHists_Company_SysDate_SysTime_TranNum(Company, SysDate, SysTime, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartTranHist item
   Description: Call UpdateExt to delete PartTranHist item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartTranHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartTranAttrValueSets(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartTranAttrValueSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartTranAttrValueSets
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets",headers=creds) as resp:
           return await resp.json()

async def post_PartTranAttrValueSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartTranAttrValueSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartTranAttrValueSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartTranAttrValueSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartTranAttrValueSets_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartTranAttrValueSet item
   Description: Calls GetByID to retrieve the PartTranAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartTranAttrValueSet
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartTranAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartTranAttrValueSets_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartTranAttrValueSet for the service
   Description: Calls UpdateExt to update PartTranAttrValueSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartTranAttrValueSet
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartTranAttrValueSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartTranAttrValueSets_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartTranAttrValueSet item
   Description: Call UpdateExt to delete PartTranAttrValueSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartTranAttrValueSet
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranHistListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartTranHist, whereClausePartTranAttrValueSet, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartTranHist=" + whereClausePartTranHist
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartTranAttrValueSet=" + whereClausePartTranAttrValueSet
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sysDate, sysTime, tranNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
   params += "sysDate=" + sysDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysTime=" + sysTime
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranNum=" + tranNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSortByList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSortByList
   Description: This method returns the Sort By selection list.
   OperationID: GetSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSortByList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunPartTranHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunPartTranHistory
   Description: This method returns the transaction history of a given part.
   OperationID: RunPartTranHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunPartTranHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunPartTranHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartTranHist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartTranHist
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartTranHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartTranHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartTranHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartTranAttrValueSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartTranAttrValueSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartTranAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartTranAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartTranAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranAttrValueSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartTranAttrValueSetRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranHistListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartTranHistListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranHistRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartTranHistRow] = obj["value"]
      pass

class Erp_Tablesets_PartTranAttrValueSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran.  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran.  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number of the related PartTran.  """  
      self.TranSeq:int = obj["TranSeq"]
      """  A system-generated number which uniquely identifies this row.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Supplier (Vendor) master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Supplier’s Purchase Point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The Supplier’s Packing Slip Number.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  Unique identifier for this Attribute Value for this receipt detail.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TranType:str = obj["TranType"]
      """   Inventory = "PUR-STK"         
JobMaterial = "PUR-MTL"
JobSubcontract = "PUR-SUB"
Other = "PUR-UKN"
Inspection = "PUR-INS"
CustomerManaged = "PUR-CMI"
SupplierManaged = "PUR-SMI"  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranHistListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RunningTotal:int = obj["RunningTotal"]
      """  Calculated Running Total  """  
      self.Packer:str = obj["Packer"]
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Dim Code Description  """  
      self.DimQty:int = obj["DimQty"]
      """  Dimension Quantity  """  
      self.TOPackID:int = obj["TOPackID"]
      """  PackID from Transfer Order Packing type  """  
      self.MiscShipPackID:int = obj["MiscShipPackID"]
      """  Miscelaneous Shipment Entry Packing ID  """  
      self.SubConShipPackID:int = obj["SubConShipPackID"]
      """  Subcontractor Shipment Packing ID  """  
      self.RunningTotalUOM:str = obj["RunningTotalUOM"]
      """  RunningTotal UOM  """  
      self.BinDescription:str = obj["BinDescription"]
      """  Description of the Bin.  """  
      self.PlantName:str = obj["PlantName"]
      """  The name of the plant.  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  Description of the warehouse  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.BinDescription:str = obj["BinDescription"]
      """  Bin Description  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Dim Code Description  """  
      self.DimQty:int = obj["DimQty"]
      """  Dimension Quantity  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.MiscShipPackID:int = obj["MiscShipPackID"]
      """  Miscelaneous Shipment Entry Packing ID  """  
      self.Packer:str = obj["Packer"]
      self.PlantName:str = obj["PlantName"]
      """  Plant Name.  """  
      self.ReasonDesc:str = obj["ReasonDesc"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RunningTotal:int = obj["RunningTotal"]
      """  Calculated Running Total  """  
      self.RunningTotalUOM:str = obj["RunningTotalUOM"]
      """  RunningTotal UOM  """  
      self.SubConShipPackID:int = obj["SubConShipPackID"]
      """  Subcontractor Shipment Packing ID  """  
      self.TOPackID:int = obj["TOPackID"]
      """  PackID from Transfer Order Packing type  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  Warehouse description.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   sysDate
   sysTime
   tranNum
   """  
   def __init__(self, obj):
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      self.tranNum:int = obj["tranNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartTranAttrValueSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran.  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran.  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction Number of the related PartTran.  """  
      self.TranSeq:int = obj["TranSeq"]
      """  A system-generated number which uniquely identifies this row.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Supplier (Vendor) master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Supplier’s Purchase Point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  The Supplier’s Packing Slip Number.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  Unique identifier for this Attribute Value for this receipt detail.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TranType:str = obj["TranType"]
      """   Inventory = "PUR-STK"         
JobMaterial = "PUR-MTL"
JobSubcontract = "PUR-SUB"
Other = "PUR-UKN"
Inspection = "PUR-INS"
CustomerManaged = "PUR-CMI"
SupplierManaged = "PUR-SMI"  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranHistListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RunningTotal:int = obj["RunningTotal"]
      """  Calculated Running Total  """  
      self.Packer:str = obj["Packer"]
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Dim Code Description  """  
      self.DimQty:int = obj["DimQty"]
      """  Dimension Quantity  """  
      self.TOPackID:int = obj["TOPackID"]
      """  PackID from Transfer Order Packing type  """  
      self.MiscShipPackID:int = obj["MiscShipPackID"]
      """  Miscelaneous Shipment Entry Packing ID  """  
      self.SubConShipPackID:int = obj["SubConShipPackID"]
      """  Subcontractor Shipment Packing ID  """  
      self.RunningTotalUOM:str = obj["RunningTotalUOM"]
      """  RunningTotal UOM  """  
      self.BinDescription:str = obj["BinDescription"]
      """  Description of the Bin.  """  
      self.PlantName:str = obj["PlantName"]
      """  The name of the plant.  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  Description of the warehouse  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranHistListTableset:
   def __init__(self, obj):
      self.PartTranHistList:list[Erp_Tablesets_PartTranHistListRow] = obj["PartTranHistList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartTranHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.BinDescription:str = obj["BinDescription"]
      """  Bin Description  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.DimCodeDesc:str = obj["DimCodeDesc"]
      """  Dim Code Description  """  
      self.DimQty:int = obj["DimQty"]
      """  Dimension Quantity  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.MiscShipPackID:int = obj["MiscShipPackID"]
      """  Miscelaneous Shipment Entry Packing ID  """  
      self.Packer:str = obj["Packer"]
      self.PlantName:str = obj["PlantName"]
      """  Plant Name.  """  
      self.ReasonDesc:str = obj["ReasonDesc"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RunningTotal:int = obj["RunningTotal"]
      """  Calculated Running Total  """  
      self.RunningTotalUOM:str = obj["RunningTotalUOM"]
      """  RunningTotal UOM  """  
      self.SubConShipPackID:int = obj["SubConShipPackID"]
      """  Subcontractor Shipment Packing ID  """  
      self.TOPackID:int = obj["TOPackID"]
      """  PackID from Transfer Order Packing type  """  
      self.WarehouseDesc:str = obj["WarehouseDesc"]
      """  Warehouse description.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranHistTableset:
   def __init__(self, obj):
      self.PartTranHist:list[Erp_Tablesets_PartTranHistRow] = obj["PartTranHist"]
      self.PartTranAttrValueSet:list[Erp_Tablesets_PartTranAttrValueSetRow] = obj["PartTranAttrValueSet"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartTranHistTableset:
   def __init__(self, obj):
      self.PartTranHist:list[Erp_Tablesets_PartTranHistRow] = obj["PartTranHist"]
      self.PartTranAttrValueSet:list[Erp_Tablesets_PartTranAttrValueSetRow] = obj["PartTranAttrValueSet"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   sysDate
   sysTime
   tranNum
   """  
   def __init__(self, obj):
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranHistTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartTranHistTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartTranHistTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartTranHistListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartTranAttrValueSet_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartTranHistTableset] = obj["ds"]
      pass

class GetNewPartTranAttrValueSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartTranHistTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartTranHist_input:
   """ Required : 
   ds
   sysDate
   sysTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartTranHistTableset] = obj["ds"]
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      pass

class GetNewPartTranHist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartTranHistTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartTranHist
   whereClausePartTranAttrValueSet
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartTranHist:str = obj["whereClausePartTranHist"]
      self.whereClausePartTranAttrValueSet:str = obj["whereClausePartTranAttrValueSet"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranHistTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSortByList_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to be processed  """  
      pass

class GetSortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.SortByList:str = obj["parameters"]
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

class RunPartTranHistory_input:
   """ Required : 
   ipPartNum
   ipPlant
   ipTranDate
   ipStartingDate
   ipLotNum
   ipDimCode
   ipSortBy
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to process  """  
      self.ipPlant:str = obj["ipPlant"]
      """  The valid Plant ID to process.  """  
      self.ipTranDate:str = obj["ipTranDate"]
      """  The Cut Off Transaction Date to process. If not supplied then the default is today.  """  
      self.ipStartingDate:str = obj["ipStartingDate"]
      """  The Starting Transaction Date to process. If not supplied then it will start with the first transaction saved.  """  
      self.ipLotNum:str = obj["ipLotNum"]
      """  The starting Lot Number to process  """  
      self.ipDimCode:str = obj["ipDimCode"]
      """  The starting Dimension Code to process  """  
      self.ipSortBy:str = obj["ipSortBy"]
      """  The sort by selected by the user.  Valid options are:
            THIST-BRW (Tran Date Browse); THISTLOT-BRW (Lot Number/Tran Date browse)
            and THISTDIM-BRW (Dim Code/Tran Date browse)  """  
      pass

class RunPartTranHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartTranHistTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartTranHistTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartTranHistTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartTranHistTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartTranHistTableset] = obj["ds"]
      pass

      """  output parameters  """  

