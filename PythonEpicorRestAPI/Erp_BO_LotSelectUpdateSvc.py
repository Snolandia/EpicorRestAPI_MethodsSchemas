import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LotSelectUpdateSvc
# Description: Generic Lot Number Selection and Update Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LotSelectUpdates(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LotSelectUpdates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LotSelectUpdates
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartLotRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates",headers=creds) as resp:
           return await resp.json()

async def post_LotSelectUpdates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LotSelectUpdates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartLotRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartLotRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LotSelectUpdates_Company_PartNum_LotNum(Company, PartNum, LotNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LotSelectUpdate item
   Description: Calls GetByID to retrieve the LotSelectUpdate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LotSelectUpdate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartLotRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LotSelectUpdates_Company_PartNum_LotNum(Company, PartNum, LotNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LotSelectUpdate for the service
   Description: Calls UpdateExt to update LotSelectUpdate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LotSelectUpdate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartLotRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LotSelectUpdates_Company_PartNum_LotNum(Company, PartNum, LotNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LotSelectUpdate item
   Description: Call UpdateExt to delete LotSelectUpdate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LotSelectUpdate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LotSelectUpdates_Company_PartNum_LotNum_PartLotAttches(Company, PartNum, LotNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PartLotAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartLotAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartLotAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")/PartLotAttches",headers=creds) as resp:
           return await resp.json()

async def get_LotSelectUpdates_Company_PartNum_LotNum_PartLotAttches_Company_PartNum_LotNum_DrawingSeq(Company, PartNum, LotNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartLotAttch item
   Description: Calls GetByID to retrieve the PartLotAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartLotAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartLotAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")/PartLotAttches(" + Company + "," + PartNum + "," + LotNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartLotAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartLotAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartLotAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartLotAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches",headers=creds) as resp:
           return await resp.json()

async def post_PartLotAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartLotAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartLotAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartLotAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartLotAttches_Company_PartNum_LotNum_DrawingSeq(Company, PartNum, LotNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartLotAttch item
   Description: Calls GetByID to retrieve the PartLotAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartLotAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartLotAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches(" + Company + "," + PartNum + "," + LotNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartLotAttches_Company_PartNum_LotNum_DrawingSeq(Company, PartNum, LotNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartLotAttch for the service
   Description: Calls UpdateExt to update PartLotAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartLotAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartLotAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches(" + Company + "," + PartNum + "," + LotNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartLotAttches_Company_PartNum_LotNum_DrawingSeq(Company, PartNum, LotNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartLotAttch item
   Description: Call UpdateExt to delete PartLotAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartLotAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param LotNum: Desc: LotNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches(" + Company + "," + PartNum + "," + LotNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartLotListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartLot, whereClausePartLotAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartLot=" + whereClausePartLot
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartLotAttch=" + whereClausePartLotAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, lotNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "lotNum=" + lotNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckDupLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDupLotNum
   Description: This method checks the Lot Number to see if there is any duplicate lot number used
by another part number.  A warning message will be returned to the user asking
if the user wants to continue creating a duplicate lot number.  This needs to be run
before Update method.  If the user answers yes to the question then the update method can be run.
   OperationID: CheckDupLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDupLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDupLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChkForNeedsLotAttrs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChkForNeedsLotAttrs
   Description: User can create a PartLot record on the fly if the user has CAN-MaintainLot permissions.
The record is created only if there is no PartLot recrod for pcLotNum and the user
has permissions.
   OperationID: ChkForNeedsLotAttrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChkForNeedsLotAttrs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChkForNeedsLotAttrs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateNewLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateNewLotNum
   Description: This method will generate a new lot number
   OperationID: GenerateNewLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateNewLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListByBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListByBinNum
   Description: This method finds lots for Parts by WarehouseCode and BinNum for PackOut Tab in CustShipEntry.
   OperationID: GetListByBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListPartLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListPartLot
   Description: This method finds lots for Parts by WarehouseCode and BinNum.
   OperationID: GetListPartLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListPartLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPartLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListByWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListByWarehouse
   Description: This method finds lots for Parts by WarehouseCode.
   OperationID: GetListByWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListByWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateLotAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateLotAttributes
   Description: Validate the attributes information introduced by the user.
   OperationID: ValidateLotAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLotAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLotAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShippingDocumentsAttached(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShippingDocumentsAttached
   Description: Validate if a Shipping Document was attached if Shipping Docs Available was marked as true
   OperationID: ValidateShippingDocumentsAttached
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShippingDocumentsAttached_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShippingDocumentsAttached_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAttributeSet
   OperationID: OnChangeAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartLot
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartLotAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartLotAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartLotAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartLotAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartLotAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartLotAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartLotListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartLotRow] = obj["value"]
      pass

class Erp_Tablesets_PartLotAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.LotNum:str = obj["LotNum"]
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

class Erp_Tablesets_PartLotListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.PartLotDescription:str = obj["PartLotDescription"]
      """  Optional lot number description.  """  
      self.OnHand:bool = obj["OnHand"]
      """  Indicates that there is still some of the lot on hand.  """  
      self.FirstRefDate:str = obj["FirstRefDate"]
      """  Earliest date that the lot was referenced.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the lot was referenced.  """  
      self.LotLaborCost:int = obj["LotLaborCost"]
      """   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.LotBurdenCost:int = obj["LotBurdenCost"]
      """  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  """  
      self.LotMaterialCost:int = obj["LotMaterialCost"]
      """  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotSubContCost:int = obj["LotSubContCost"]
      """  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotMtlBurCost:int = obj["LotMtlBurCost"]
      """  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Determined by setting on Part.AttExpDt if required or tracked.  """  
      self.ShipDocAvail:bool = obj["ShipDocAvail"]
      """  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  """  
      self.Batch:str = obj["Batch"]
      """  Determined by setting on Part.AttBatch if required or tracked.  """  
      self.MfgBatch:str = obj["MfgBatch"]
      """  Determined by setting on Part.AttMfgBatch if required or tracked.  """  
      self.MfgLot:str = obj["MfgLot"]
      """  Determined by setting on Part.AttMfgLot if required or tracked.  """  
      self.HeatNum:str = obj["HeatNum"]
      """  Determined by setting on Part.AttHeat if required or tracked.  """  
      self.FirmWare:str = obj["FirmWare"]
      """  Determined by setting on Part.AttFirmware if required or tracked.  """  
      self.BestBeforeDt:str = obj["BestBeforeDt"]
      """  Determined by setting on Part.AttBeforeDt if required or tracked.  """  
      self.MfgDt:str = obj["MfgDt"]
      """  Determined by setting on Part.AttMfgDt if required or tracked.  """  
      self.CureDt:str = obj["CureDt"]
      """  Determined by setting on Part.AttCureDt if required or tracked.  """  
      self.ExpireDt:str = obj["ExpireDt"]
      """  Expire Date  """  
      self.FIFOLotLaborCost:int = obj["FIFOLotLaborCost"]
      """   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOLotBurdenCost:int = obj["FIFOLotBurdenCost"]
      """  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  """  
      self.FIFOLotMaterialCost:int = obj["FIFOLotMaterialCost"]
      """  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotSubContCost:int = obj["FIFOLotSubContCost"]
      """  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotMtlBurCost:int = obj["FIFOLotMtlBurCost"]
      """  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.CSFLMWComOath:str = obj["CSFLMWComOath"]
      """   Malaysia Localization
LMW Commissioner of Oath's Number  """  
      self.CSFCJ5FormNbr:str = obj["CSFCJ5FormNbr"]
      """   Malaysia Localization
CJ5 Form Number  """  
      self.CSFCJ5Vessel:str = obj["CSFCJ5Vessel"]
      """   Malaysia Localization
CJ5 Vessel Number  """  
      self.CSFCJ5ApvlStart:str = obj["CSFCJ5ApvlStart"]
      """   Malaysia Localization
The start date of CJ5 approved period  """  
      self.CSFCJ5ApvlEnd:str = obj["CSFCJ5ApvlEnd"]
      """   Malaysia Localization
The end date of CJ5 approved period  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TransactionSource:str = obj["TransactionSource"]
      """  Source of transaction  """  
      self.ScrLotBurdenCost:int = obj["ScrLotBurdenCost"]
      self.ScrLotLaborCost:int = obj["ScrLotLaborCost"]
      self.ScrLotMaterialCost:int = obj["ScrLotMaterialCost"]
      self.ScrLotMtlBurCost:int = obj["ScrLotMtlBurCost"]
      self.ScrLotSubContCost:int = obj["ScrLotSubContCost"]
      self.Plant:str = obj["Plant"]
      """  Plant to which the lot belongs to  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  On Hand quantity for the part in the specified lot  """  
      self.CSFCJ5Avail:bool = obj["CSFCJ5Avail"]
      """   Malaysia localization         
Indicated if CSF fields are available  """  
      self.CSFLMWAvail:bool = obj["CSFLMWAvail"]
      """   Malaysia localization         
Indicates if LMW fields are available  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartLotRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.PartLotDescription:str = obj["PartLotDescription"]
      """  Optional lot number description.  """  
      self.OnHand:bool = obj["OnHand"]
      """  Indicates that there is still some of the lot on hand.  """  
      self.FirstRefDate:str = obj["FirstRefDate"]
      """  Earliest date that the lot was referenced.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the lot was referenced.  """  
      self.LotLaborCost:int = obj["LotLaborCost"]
      """   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.LotBurdenCost:int = obj["LotBurdenCost"]
      """  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  """  
      self.LotMaterialCost:int = obj["LotMaterialCost"]
      """  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotSubContCost:int = obj["LotSubContCost"]
      """  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotMtlBurCost:int = obj["LotMtlBurCost"]
      """  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Determined by setting on Part.AttExpDt if required or tracked.  """  
      self.ShipDocAvail:bool = obj["ShipDocAvail"]
      """  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  """  
      self.Batch:str = obj["Batch"]
      """  Determined by setting on Part.AttBatch if required or tracked.  """  
      self.MfgBatch:str = obj["MfgBatch"]
      """  Determined by setting on Part.AttMfgBatch if required or tracked.  """  
      self.MfgLot:str = obj["MfgLot"]
      """  Determined by setting on Part.AttMfgLot if required or tracked.  """  
      self.HeatNum:str = obj["HeatNum"]
      """  Determined by setting on Part.AttHeat if required or tracked.  """  
      self.FirmWare:str = obj["FirmWare"]
      """  Determined by setting on Part.AttFirmware if required or tracked.  """  
      self.BestBeforeDt:str = obj["BestBeforeDt"]
      """  Determined by setting on Part.AttBeforeDt if required or tracked.  """  
      self.MfgDt:str = obj["MfgDt"]
      """  Determined by setting on Part.AttMfgDt if required or tracked.  """  
      self.CureDt:str = obj["CureDt"]
      """  Determined by setting on Part.AttCureDt if required or tracked.  """  
      self.ExpireDt:str = obj["ExpireDt"]
      """  Expire Date  """  
      self.FIFOLotLaborCost:int = obj["FIFOLotLaborCost"]
      """   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOLotBurdenCost:int = obj["FIFOLotBurdenCost"]
      """  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  """  
      self.FIFOLotMaterialCost:int = obj["FIFOLotMaterialCost"]
      """  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotSubContCost:int = obj["FIFOLotSubContCost"]
      """  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotMtlBurCost:int = obj["FIFOLotMtlBurCost"]
      """  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.CSFLMWComOath:str = obj["CSFLMWComOath"]
      """   Malaysia Localization
LMW Commissioner of Oath's Number  """  
      self.CSFCJ5FormNbr:str = obj["CSFCJ5FormNbr"]
      """   Malaysia Localization
CJ5 Form Number  """  
      self.CSFCJ5Vessel:str = obj["CSFCJ5Vessel"]
      """   Malaysia Localization
CJ5 Vessel Number  """  
      self.CSFCJ5ApvlStart:str = obj["CSFCJ5ApvlStart"]
      """   Malaysia Localization
The start date of CJ5 approved period  """  
      self.CSFCJ5ApvlEnd:str = obj["CSFCJ5ApvlEnd"]
      """   Malaysia Localization
The end date of CJ5 approved period  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXImportLocation:str = obj["MXImportLocation"]
      """  MXImportLocation  """  
      self.MXImportDate:str = obj["MXImportDate"]
      """  MXImportDate  """  
      self.TotalQtyAvg:int = obj["TotalQtyAvg"]
      """  Total OnHand Quantity used specific for Average Costing calculations  """  
      self.ISOrigCountryNum:int = obj["ISOrigCountryNum"]
      """  Country number of the Origin Country (defaults from Part Country of Origin).  """  
      self.CSFLMWAvail:bool = obj["CSFLMWAvail"]
      """   Malaysia localization         
Indicates if LMW fields are available  """  
      self.DeferManual:bool = obj["DeferManual"]
      """  Indicates if the Lot is created from LotEntry, used for Defer functionality.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  On Hand quantity for the part in the specified lot  """  
      self.Plant:str = obj["Plant"]
      """  Plant to which the lot belongs to  """  
      self.ScrLotBurdenCost:int = obj["ScrLotBurdenCost"]
      self.ScrLotLaborCost:int = obj["ScrLotLaborCost"]
      self.ScrLotMaterialCost:int = obj["ScrLotMaterialCost"]
      self.ScrLotMtlBurCost:int = obj["ScrLotMtlBurCost"]
      self.ScrLotSubContCost:int = obj["ScrLotSubContCost"]
      self.TransactionSource:str = obj["TransactionSource"]
      """  Source of transaction  """  
      self.CSFCJ5Avail:bool = obj["CSFCJ5Avail"]
      """   Malaysia localization         
Indicated if CSF fields are available  """  
      self.IUM:str = obj["IUM"]
      """  Part UOM Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ISOrigCntyDescription:str = obj["ISOrigCntyDescription"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckDupLotNum_input:
   """ Required : 
   vLotNum
   vPartNum
   vRowid
   """  
   def __init__(self, obj):
      self.vLotNum:str = obj["vLotNum"]
      """  The Lot Number to be checked for duplicate  """  
      self.vPartNum:str = obj["vPartNum"]
      """  Part Number associated with the current Lot Number  """  
      self.vRowid:str = obj["vRowid"]
      """  RowIdent field of the PartLot  """  
      pass

class CheckDupLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChkForNeedsLotAttrs_input:
   """ Required : 
   pcPartNum
   pcLotNum
   pcDeferOption
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      self.pcLotNum:str = obj["pcLotNum"]
      self.pcDeferOption:str = obj["pcDeferOption"]
      pass

class ChkForNeedsLotAttrs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.needsLotAttrs:bool = obj["needsLotAttrs"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   partNum
   lotNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.lotNum:str = obj["lotNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_LotSelectUpdateTableset:
   def __init__(self, obj):
      self.PartLot:list[Erp_Tablesets_PartLotRow] = obj["PartLot"]
      self.PartLotAttch:list[Erp_Tablesets_PartLotAttchRow] = obj["PartLotAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartLotAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.LotNum:str = obj["LotNum"]
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

class Erp_Tablesets_PartLotListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.PartLotDescription:str = obj["PartLotDescription"]
      """  Optional lot number description.  """  
      self.OnHand:bool = obj["OnHand"]
      """  Indicates that there is still some of the lot on hand.  """  
      self.FirstRefDate:str = obj["FirstRefDate"]
      """  Earliest date that the lot was referenced.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the lot was referenced.  """  
      self.LotLaborCost:int = obj["LotLaborCost"]
      """   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.LotBurdenCost:int = obj["LotBurdenCost"]
      """  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  """  
      self.LotMaterialCost:int = obj["LotMaterialCost"]
      """  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotSubContCost:int = obj["LotSubContCost"]
      """  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotMtlBurCost:int = obj["LotMtlBurCost"]
      """  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Determined by setting on Part.AttExpDt if required or tracked.  """  
      self.ShipDocAvail:bool = obj["ShipDocAvail"]
      """  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  """  
      self.Batch:str = obj["Batch"]
      """  Determined by setting on Part.AttBatch if required or tracked.  """  
      self.MfgBatch:str = obj["MfgBatch"]
      """  Determined by setting on Part.AttMfgBatch if required or tracked.  """  
      self.MfgLot:str = obj["MfgLot"]
      """  Determined by setting on Part.AttMfgLot if required or tracked.  """  
      self.HeatNum:str = obj["HeatNum"]
      """  Determined by setting on Part.AttHeat if required or tracked.  """  
      self.FirmWare:str = obj["FirmWare"]
      """  Determined by setting on Part.AttFirmware if required or tracked.  """  
      self.BestBeforeDt:str = obj["BestBeforeDt"]
      """  Determined by setting on Part.AttBeforeDt if required or tracked.  """  
      self.MfgDt:str = obj["MfgDt"]
      """  Determined by setting on Part.AttMfgDt if required or tracked.  """  
      self.CureDt:str = obj["CureDt"]
      """  Determined by setting on Part.AttCureDt if required or tracked.  """  
      self.ExpireDt:str = obj["ExpireDt"]
      """  Expire Date  """  
      self.FIFOLotLaborCost:int = obj["FIFOLotLaborCost"]
      """   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOLotBurdenCost:int = obj["FIFOLotBurdenCost"]
      """  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  """  
      self.FIFOLotMaterialCost:int = obj["FIFOLotMaterialCost"]
      """  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotSubContCost:int = obj["FIFOLotSubContCost"]
      """  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotMtlBurCost:int = obj["FIFOLotMtlBurCost"]
      """  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.CSFLMWComOath:str = obj["CSFLMWComOath"]
      """   Malaysia Localization
LMW Commissioner of Oath's Number  """  
      self.CSFCJ5FormNbr:str = obj["CSFCJ5FormNbr"]
      """   Malaysia Localization
CJ5 Form Number  """  
      self.CSFCJ5Vessel:str = obj["CSFCJ5Vessel"]
      """   Malaysia Localization
CJ5 Vessel Number  """  
      self.CSFCJ5ApvlStart:str = obj["CSFCJ5ApvlStart"]
      """   Malaysia Localization
The start date of CJ5 approved period  """  
      self.CSFCJ5ApvlEnd:str = obj["CSFCJ5ApvlEnd"]
      """   Malaysia Localization
The end date of CJ5 approved period  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TransactionSource:str = obj["TransactionSource"]
      """  Source of transaction  """  
      self.ScrLotBurdenCost:int = obj["ScrLotBurdenCost"]
      self.ScrLotLaborCost:int = obj["ScrLotLaborCost"]
      self.ScrLotMaterialCost:int = obj["ScrLotMaterialCost"]
      self.ScrLotMtlBurCost:int = obj["ScrLotMtlBurCost"]
      self.ScrLotSubContCost:int = obj["ScrLotSubContCost"]
      self.Plant:str = obj["Plant"]
      """  Plant to which the lot belongs to  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  On Hand quantity for the part in the specified lot  """  
      self.CSFCJ5Avail:bool = obj["CSFCJ5Avail"]
      """   Malaysia localization         
Indicated if CSF fields are available  """  
      self.CSFLMWAvail:bool = obj["CSFLMWAvail"]
      """   Malaysia localization         
Indicates if LMW fields are available  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartLotListTableset:
   def __init__(self, obj):
      self.PartLotList:list[Erp_Tablesets_PartLotListRow] = obj["PartLotList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartLotRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.PartLotDescription:str = obj["PartLotDescription"]
      """  Optional lot number description.  """  
      self.OnHand:bool = obj["OnHand"]
      """  Indicates that there is still some of the lot on hand.  """  
      self.FirstRefDate:str = obj["FirstRefDate"]
      """  Earliest date that the lot was referenced.  """  
      self.LastRefDate:str = obj["LastRefDate"]
      """  Latest date that the lot was referenced.  """  
      self.LotLaborCost:int = obj["LotLaborCost"]
      """   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.LotBurdenCost:int = obj["LotBurdenCost"]
      """  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  """  
      self.LotMaterialCost:int = obj["LotMaterialCost"]
      """  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotSubContCost:int = obj["LotSubContCost"]
      """  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.LotMtlBurCost:int = obj["LotMtlBurCost"]
      """  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  """  
      self.ExpirationDate:str = obj["ExpirationDate"]
      """  Determined by setting on Part.AttExpDt if required or tracked.  """  
      self.ShipDocAvail:bool = obj["ShipDocAvail"]
      """  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  """  
      self.Batch:str = obj["Batch"]
      """  Determined by setting on Part.AttBatch if required or tracked.  """  
      self.MfgBatch:str = obj["MfgBatch"]
      """  Determined by setting on Part.AttMfgBatch if required or tracked.  """  
      self.MfgLot:str = obj["MfgLot"]
      """  Determined by setting on Part.AttMfgLot if required or tracked.  """  
      self.HeatNum:str = obj["HeatNum"]
      """  Determined by setting on Part.AttHeat if required or tracked.  """  
      self.FirmWare:str = obj["FirmWare"]
      """  Determined by setting on Part.AttFirmware if required or tracked.  """  
      self.BestBeforeDt:str = obj["BestBeforeDt"]
      """  Determined by setting on Part.AttBeforeDt if required or tracked.  """  
      self.MfgDt:str = obj["MfgDt"]
      """  Determined by setting on Part.AttMfgDt if required or tracked.  """  
      self.CureDt:str = obj["CureDt"]
      """  Determined by setting on Part.AttCureDt if required or tracked.  """  
      self.ExpireDt:str = obj["ExpireDt"]
      """  Expire Date  """  
      self.FIFOLotLaborCost:int = obj["FIFOLotLaborCost"]
      """   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  """  
      self.FIFOLotBurdenCost:int = obj["FIFOLotBurdenCost"]
      """  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  """  
      self.FIFOLotMaterialCost:int = obj["FIFOLotMaterialCost"]
      """  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotSubContCost:int = obj["FIFOLotSubContCost"]
      """  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.FIFOLotMtlBurCost:int = obj["FIFOLotMtlBurCost"]
      """  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  """  
      self.CSFLMWComOath:str = obj["CSFLMWComOath"]
      """   Malaysia Localization
LMW Commissioner of Oath's Number  """  
      self.CSFCJ5FormNbr:str = obj["CSFCJ5FormNbr"]
      """   Malaysia Localization
CJ5 Form Number  """  
      self.CSFCJ5Vessel:str = obj["CSFCJ5Vessel"]
      """   Malaysia Localization
CJ5 Vessel Number  """  
      self.CSFCJ5ApvlStart:str = obj["CSFCJ5ApvlStart"]
      """   Malaysia Localization
The start date of CJ5 approved period  """  
      self.CSFCJ5ApvlEnd:str = obj["CSFCJ5ApvlEnd"]
      """   Malaysia Localization
The end date of CJ5 approved period  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXImportLocation:str = obj["MXImportLocation"]
      """  MXImportLocation  """  
      self.MXImportDate:str = obj["MXImportDate"]
      """  MXImportDate  """  
      self.TotalQtyAvg:int = obj["TotalQtyAvg"]
      """  Total OnHand Quantity used specific for Average Costing calculations  """  
      self.ISOrigCountryNum:int = obj["ISOrigCountryNum"]
      """  Country number of the Origin Country (defaults from Part Country of Origin).  """  
      self.CSFLMWAvail:bool = obj["CSFLMWAvail"]
      """   Malaysia localization         
Indicates if LMW fields are available  """  
      self.DeferManual:bool = obj["DeferManual"]
      """  Indicates if the Lot is created from LotEntry, used for Defer functionality.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  On Hand quantity for the part in the specified lot  """  
      self.Plant:str = obj["Plant"]
      """  Plant to which the lot belongs to  """  
      self.ScrLotBurdenCost:int = obj["ScrLotBurdenCost"]
      self.ScrLotLaborCost:int = obj["ScrLotLaborCost"]
      self.ScrLotMaterialCost:int = obj["ScrLotMaterialCost"]
      self.ScrLotMtlBurCost:int = obj["ScrLotMtlBurCost"]
      self.ScrLotSubContCost:int = obj["ScrLotSubContCost"]
      self.TransactionSource:str = obj["TransactionSource"]
      """  Source of transaction  """  
      self.CSFCJ5Avail:bool = obj["CSFCJ5Avail"]
      """   Malaysia localization         
Indicated if CSF fields are available  """  
      self.IUM:str = obj["IUM"]
      """  Part UOM Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ISOrigCntyDescription:str = obj["ISOrigCntyDescription"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtLotSelectUpdateTableset:
   def __init__(self, obj):
      self.PartLot:list[Erp_Tablesets_PartLotRow] = obj["PartLot"]
      self.PartLotAttch:list[Erp_Tablesets_PartLotAttchRow] = obj["PartLotAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateNewLotNum_input:
   """ Required : 
   vPartNum
   """  
   def __init__(self, obj):
      self.vPartNum:str = obj["vPartNum"]
      """  Part Number associated with the current Lot Number  """  
      pass

class GenerateNewLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vNewLotNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   partNum
   lotNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.lotNum:str = obj["lotNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["returnObj"]
      pass

class GetListByBinNum_input:
   """ Required : 
   ipWarehouseCode
   ipBinNum
   whereclause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code.  """  
      self.ipBinNum:str = obj["ipBinNum"]
      """  Bin number.  """  
      self.whereclause:str = obj["whereclause"]
      """  WhereClause.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListByBinNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartLotListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListByWarehouse_input:
   """ Required : 
   ipWarehouseCode
   ipPartNum
   ipUOMCode
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  PartNum.  """  
      self.ipUOMCode:str = obj["ipUOMCode"]
      """  UOMCode.  """  
      pass

class GetListByWarehouse_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartLotListTableset] = obj["returnObj"]
      pass

class GetListPartLot_input:
   """ Required : 
   ipWarehouseCode
   ipBinNum
   attributeSetID
   whereclause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code.  """  
      self.ipBinNum:str = obj["ipBinNum"]
      """  Bin number.  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID  """  
      self.whereclause:str = obj["whereclause"]
      """  WhereClause.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListPartLot_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartLotListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_PartLotListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartLotAttch_input:
   """ Required : 
   ds
   partNum
   lotNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.lotNum:str = obj["lotNum"]
      pass

class GetNewPartLotAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartLot_input:
   """ Required : 
   ds
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewPartLot_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartLot
   whereClausePartLotAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartLot:str = obj["whereClausePartLot"]
      self.whereClausePartLotAttch:str = obj["whereClausePartLotAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["returnObj"]
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

class OnChangeAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

class OnChangeAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      self.DynAttrValueSetDescription:str = obj["parameters"]
      self.DynAttrValueSetShortDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.revisionNum:str = obj["parameters"]
      self.AttributeSetID:int = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   partNum
   AttributeSetID
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.partNum:str = obj["partNum"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AttributeSetID:int = obj["parameters"]
      self.DynAttrValueSetDescription:str = obj["parameters"]
      self.DynAttrValueSetShortDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLotSelectUpdateTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLotSelectUpdateTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateLotAttributes_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

class ValidateLotAttributes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateShippingDocumentsAttached_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

class ValidateShippingDocumentsAttached_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LotSelectUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

