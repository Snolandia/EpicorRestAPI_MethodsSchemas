import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AssetImpairSvc
# Description: Fixed Asset Impairment
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AssetImpairs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AssetImpairs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AssetImpairs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAImpairmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs",headers=creds) as resp:
           return await resp.json()

async def post_AssetImpairs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AssetImpairs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAImpairmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAImpairmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AssetImpairs_Company_AssetNum_ImpairNum(Company, AssetNum, ImpairNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AssetImpair item
   Description: Calls GetByID to retrieve the AssetImpair item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AssetImpair
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param ImpairNum: Desc: ImpairNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAImpairmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AssetImpairs_Company_AssetNum_ImpairNum(Company, AssetNum, ImpairNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AssetImpair for the service
   Description: Calls UpdateExt to update AssetImpair. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AssetImpair
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param ImpairNum: Desc: ImpairNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAImpairmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AssetImpairs_Company_AssetNum_ImpairNum(Company, AssetNum, ImpairNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AssetImpair item
   Description: Call UpdateExt to delete AssetImpair item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AssetImpair
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param ImpairNum: Desc: ImpairNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_AssetImpairs_Company_AssetNum_ImpairNum_FAImpairmentAttches(Company, AssetNum, ImpairNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FAImpairmentAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAImpairmentAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param ImpairNum: Desc: ImpairNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAImpairmentAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")/FAImpairmentAttches",headers=creds) as resp:
           return await resp.json()

async def get_AssetImpairs_Company_AssetNum_ImpairNum_FAImpairmentAttches_Company_AssetNum_ImpairNum_DrawingSeq(Company, AssetNum, ImpairNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAImpairmentAttch item
   Description: Calls GetByID to retrieve the FAImpairmentAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAImpairmentAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param ImpairNum: Desc: ImpairNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")/FAImpairmentAttches(" + Company + "," + AssetNum + "," + ImpairNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAImpairmentAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAImpairmentAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAImpairmentAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAImpairmentAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches",headers=creds) as resp:
           return await resp.json()

async def post_FAImpairmentAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAImpairmentAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAImpairmentAttches_Company_AssetNum_ImpairNum_DrawingSeq(Company, AssetNum, ImpairNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAImpairmentAttch item
   Description: Calls GetByID to retrieve the FAImpairmentAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAImpairmentAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param ImpairNum: Desc: ImpairNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches(" + Company + "," + AssetNum + "," + ImpairNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAImpairmentAttches_Company_AssetNum_ImpairNum_DrawingSeq(Company, AssetNum, ImpairNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAImpairmentAttch for the service
   Description: Calls UpdateExt to update FAImpairmentAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAImpairmentAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param ImpairNum: Desc: ImpairNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches(" + Company + "," + AssetNum + "," + ImpairNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAImpairmentAttches_Company_AssetNum_ImpairNum_DrawingSeq(Company, AssetNum, ImpairNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAImpairmentAttch item
   Description: Call UpdateExt to delete FAImpairmentAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAImpairmentAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param ImpairNum: Desc: ImpairNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches(" + Company + "," + AssetNum + "," + ImpairNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAImpairmentListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFAImpairment, whereClauseFAImpairmentAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFAImpairment=" + whereClauseFAImpairment
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFAImpairmentAttch=" + whereClauseFAImpairmentAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetNum, impairNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "assetNum=" + assetNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "impairNum=" + impairNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckAssetTransactions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAssetTransactions
   Description: Checks if there are any transactions for this Asset marked as Ready To Post
   OperationID: CheckAssetTransactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearReadyToPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearReadyToPost
   Description: Clears Ready To Post flag on Asset transactions with SysRowID different from the one provided
   OperationID: ClearReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeImpairmentCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeImpairmentCost
   Description: Method to call when changing the impairment cost.
   OperationID: ChangeImpairmentCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeImpairmentCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeImpairmentCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAssetDepRecalcNeeded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAssetDepRecalcNeeded
   Description: Check if the asset or any of its registers requires depreciation calculation
   OperationID: CheckAssetDepRecalcNeeded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetDepRecalcNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetDepRecalcNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAImpairment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAImpairment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAImpairment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAImpairment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAImpairment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAImpairmentAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAImpairmentAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAImpairmentAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAImpairmentAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAImpairmentAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAImpairmentAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAImpairmentListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAImpairmentRow] = obj["value"]
      pass

class Erp_Tablesets_FAImpairmentAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.ImpairNum:int = obj["ImpairNum"]
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

class Erp_Tablesets_FAImpairmentListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.ImpairNum:int = obj["ImpairNum"]
      """  Unique number to identify the Impairment of an asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Impairment.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The Impairment Date that will be used to get the exchange rate.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the impairment is allowed to be posted to the GL.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the impairment to the GL.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.ImpairmentCost:int = obj["ImpairmentCost"]
      """  The impairment cost recorded against the asset.  """  
      self.DocImpairmentCost:int = obj["DocImpairmentCost"]
      """  The impairment cost recorded against the asset in the currency specified.  """  
      self.Rpt1ImpairmentCost:int = obj["Rpt1ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.Rpt2ImpairmentCost:int = obj["Rpt2ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.Rpt3ImpairmentCost:int = obj["Rpt3ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of posting of the addition to the GL.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of posting of the addition to the GL.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the impairment is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the impairment is posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.IsLocked:bool = obj["IsLocked"]
      """  Shows if this impairment transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means the entry can not be updated or deleted: the impairment is already in review journal or in posting process.  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAImpairmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.ImpairNum:int = obj["ImpairNum"]
      """  Unique number to identify the Impairment of an asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Impairment.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The Impairment Date that will be used to get the exchange rate.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the impairment is allowed to be posted to the GL.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the impairment to the GL.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.ImpairmentCost:int = obj["ImpairmentCost"]
      """  The impairment cost recorded against the asset.  """  
      self.DocImpairmentCost:int = obj["DocImpairmentCost"]
      """  The impairment cost recorded against the asset in the currency specified.  """  
      self.Rpt1ImpairmentCost:int = obj["Rpt1ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.Rpt2ImpairmentCost:int = obj["Rpt2ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.Rpt3ImpairmentCost:int = obj["Rpt3ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of posting of the addition to the GL.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of posting of the addition to the GL.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the impairment is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the impairment is posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.IsLocked:bool = obj["IsLocked"]
      """  Shows if this impairment transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means the entry can not be updated or deleted: the impairment is already in review journal or in posting process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeImpairmentCost_input:
   """ Required : 
   ProposedImpairCost
   BaseOrDoc
   ds
   """  
   def __init__(self, obj):
      self.ProposedImpairCost:int = obj["ProposedImpairCost"]
      """  The proposed impairment cost  """  
      self.BaseOrDoc:str = obj["BaseOrDoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_AssetImpairTableset] = obj["ds"]
      pass

class ChangeImpairmentCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetImpairTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckAssetDepRecalcNeeded_input:
   """ Required : 
   assetNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      pass

class CheckAssetDepRecalcNeeded_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if depreciation calculation is required  """  
      pass

class CheckAssetTransactions_input:
   """ Required : 
   assetNum
   sysRowID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID to be excluded from search  """  
      pass

class CheckAssetTransactions_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  If transaction found: Warning message offering to clear Ready To Post flag; otherwise: an empty string  """  
      pass

class ClearReadyToPost_input:
   """ Required : 
   assetNum
   sysRowID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID to be excluded from search  """  
      pass

class ClearReadyToPost_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   assetNum
   impairNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.impairNum:int = obj["impairNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AssetImpairTableset:
   def __init__(self, obj):
      self.FAImpairment:list[Erp_Tablesets_FAImpairmentRow] = obj["FAImpairment"]
      self.FAImpairmentAttch:list[Erp_Tablesets_FAImpairmentAttchRow] = obj["FAImpairmentAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FAImpairmentAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.ImpairNum:int = obj["ImpairNum"]
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

class Erp_Tablesets_FAImpairmentListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.ImpairNum:int = obj["ImpairNum"]
      """  Unique number to identify the Impairment of an asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Impairment.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The Impairment Date that will be used to get the exchange rate.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the impairment is allowed to be posted to the GL.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the impairment to the GL.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.ImpairmentCost:int = obj["ImpairmentCost"]
      """  The impairment cost recorded against the asset.  """  
      self.DocImpairmentCost:int = obj["DocImpairmentCost"]
      """  The impairment cost recorded against the asset in the currency specified.  """  
      self.Rpt1ImpairmentCost:int = obj["Rpt1ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.Rpt2ImpairmentCost:int = obj["Rpt2ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.Rpt3ImpairmentCost:int = obj["Rpt3ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of posting of the addition to the GL.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of posting of the addition to the GL.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the impairment is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the impairment is posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.IsLocked:bool = obj["IsLocked"]
      """  Shows if this impairment transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means the entry can not be updated or deleted: the impairment is already in review journal or in posting process.  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAImpairmentListTableset:
   def __init__(self, obj):
      self.FAImpairmentList:list[Erp_Tablesets_FAImpairmentListRow] = obj["FAImpairmentList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FAImpairmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.ImpairNum:int = obj["ImpairNum"]
      """  Unique number to identify the Impairment of an asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Impairment.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The Impairment Date that will be used to get the exchange rate.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the impairment is allowed to be posted to the GL.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the impairment to the GL.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.ImpairmentCost:int = obj["ImpairmentCost"]
      """  The impairment cost recorded against the asset.  """  
      self.DocImpairmentCost:int = obj["DocImpairmentCost"]
      """  The impairment cost recorded against the asset in the currency specified.  """  
      self.Rpt1ImpairmentCost:int = obj["Rpt1ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.Rpt2ImpairmentCost:int = obj["Rpt2ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.Rpt3ImpairmentCost:int = obj["Rpt3ImpairmentCost"]
      """  Reporting currency value of the Impairment Cost.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of posting of the addition to the GL.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of posting of the addition to the GL.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the impairment is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the impairment is posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      self.IsLocked:bool = obj["IsLocked"]
      """  Shows if this impairment transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means the entry can not be updated or deleted: the impairment is already in review journal or in posting process.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAssetImpairTableset:
   def __init__(self, obj):
      self.FAImpairment:list[Erp_Tablesets_FAImpairmentRow] = obj["FAImpairment"]
      self.FAImpairmentAttch:list[Erp_Tablesets_FAImpairmentAttchRow] = obj["FAImpairmentAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   assetNum
   impairNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.impairNum:int = obj["impairNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AssetImpairTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AssetImpairTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AssetImpairTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAImpairmentListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFAImpairmentAttch_input:
   """ Required : 
   ds
   assetNum
   impairNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetImpairTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.impairNum:int = obj["impairNum"]
      pass

class GetNewFAImpairmentAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetImpairTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFAImpairment_input:
   """ Required : 
   ds
   assetNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetImpairTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      pass

class GetNewFAImpairment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetImpairTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFAImpairment
   whereClauseFAImpairmentAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFAImpairment:str = obj["whereClauseFAImpairment"]
      self.whereClauseFAImpairmentAttch:str = obj["whereClauseFAImpairmentAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AssetImpairTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAssetImpairTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAssetImpairTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetImpairTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetImpairTableset] = obj["ds"]
      pass

      """  output parameters  """  

