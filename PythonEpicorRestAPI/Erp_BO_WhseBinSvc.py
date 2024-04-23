import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.WhseBinSvc
# Description: Warehouse Bin
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_WhseBins(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseBins items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseBins
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins",headers=creds) as resp:
           return await resp.json()

async def post_WhseBins(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseBinRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseBinRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseBins_Company_WarehouseCode_BinNum(Company, WarehouseCode, BinNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseBin item
   Description: Calls GetByID to retrieve the WhseBin item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseBinRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseBins_Company_WarehouseCode_BinNum(Company, WarehouseCode, BinNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseBin for the service
   Description: Calls UpdateExt to update WhseBin. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseBinRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseBins_Company_WarehouseCode_BinNum(Company, WarehouseCode, BinNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseBin item
   Description: Call UpdateExt to delete WhseBin item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseBin
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseBins_Company_WarehouseCode_BinNum_WhseBinAttches(Company, WarehouseCode, BinNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhseBinAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhseBinAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseBinAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")/WhseBinAttches",headers=creds) as resp:
           return await resp.json()

async def get_WhseBins_Company_WarehouseCode_BinNum_WhseBinAttches_Company_WarehouseCode_BinNum_DrawingSeq(Company, WarehouseCode, BinNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseBinAttch item
   Description: Calls GetByID to retrieve the WhseBinAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseBinAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBins(" + Company + "," + WarehouseCode + "," + BinNum + ")/WhseBinAttches(" + Company + "," + WarehouseCode + "," + BinNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhseBinAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhseBinAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhseBinAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseBinAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches",headers=creds) as resp:
           return await resp.json()

async def post_WhseBinAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhseBinAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhseBinAttches_Company_WarehouseCode_BinNum_DrawingSeq(Company, WarehouseCode, BinNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhseBinAttch item
   Description: Calls GetByID to retrieve the WhseBinAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhseBinAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches(" + Company + "," + WarehouseCode + "," + BinNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhseBinAttches_Company_WarehouseCode_BinNum_DrawingSeq(Company, WarehouseCode, BinNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhseBinAttch for the service
   Description: Calls UpdateExt to update WhseBinAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhseBinAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhseBinAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches(" + Company + "," + WarehouseCode + "," + BinNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhseBinAttches_Company_WarehouseCode_BinNum_DrawingSeq(Company, WarehouseCode, BinNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhseBinAttch item
   Description: Call UpdateExt to delete WhseBinAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhseBinAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param BinNum: Desc: BinNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/WhseBinAttches(" + Company + "," + WarehouseCode + "," + BinNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhseBinListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseWhseBin, whereClauseWhseBinAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseWhseBin=" + whereClauseWhseBin
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhseBinAttch=" + whereClauseWhseBinAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(warehouseCode, binNum, epicorHeaders = None):
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
   params += "warehouseCode=" + warehouseCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "binNum=" + binNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddNewWhseBinFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddNewWhseBinFormat
   Description: Add a New record in WhseBinFormat table
   OperationID: AddNewWhseBinFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewWhseBinFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewWhseBinFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CommitGeneratedBins(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CommitGeneratedBins
   Description: Commit to database the proposed Bin Numbers selected
   OperationID: CommitGeneratedBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitGeneratedBins_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitGeneratedBins_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateBinFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateBinFormat
   Description: Generates the Bin format according to the segments defined
   OperationID: GenerateBinFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateBinFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBinFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateBins(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateBins
   Description: Create Bin numbers according to the specified format
   OperationID: GenerateBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateBins_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBins_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCustID
   Description: OnChangeCustId
   OperationID: OnChangeCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InActiveFlag(epicorHeaders = None):
   """  
   Summary: Invoke method InActiveFlag
   Description: OnChangeInActive
   OperationID: InActiveFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/InActiveFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSuppID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSuppID
   Description: OnChangeSuppId
   OperationID: OnChangeSuppID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSuppID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSuppID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWhseBinWizardCustId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWhseBinWizardCustId
   Description: OnChangeWhseBinWizardCustId
   OperationID: OnChangeWhseBinWizardCustId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinWizardCustId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinWizardCustId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWhseBinWizardSuppId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWhseBinWizardSuppId
   Description: OnChangeWhseBinWizardSuppId
   OperationID: OnChangeWhseBinWizardSuppId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWhseBinWizardSuppId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWhseBinWizardSuppId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSegmentMaximum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSegmentMaximum
   Description: Execute necessary modifications when Maximum value is changed for the segment
   OperationID: OnChangingSegmentMaximum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSegmentMaximum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSegmentMaximum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSegmentMinimum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSegmentMinimum
   Description: Execute necessary modifications when Minimum value is changed for the segment
   OperationID: OnChangingSegmentMinimum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSegmentMinimum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSegmentMinimum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSegmentPositions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSegmentPositions
   Description: Execute necessary modifications when Number of Positions is changed for the Segment
   OperationID: OnChangingSegmentPositions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSegmentPositions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSegmentPositions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSegmentType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSegmentType
   Description: Execute necessary modifications when Segment Type is changed
   OperationID: OnChangingSegmentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSegmentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSegmentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseBin
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhseBinAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhseBinAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhseBinAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhseBinAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhseBinAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WhseBinSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseBinAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseBinListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhseBinRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhseBinRow] = obj["value"]
      pass

class Erp_Tablesets_WhseBinAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
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

class Erp_Tablesets_WhseBinListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.Description:str = obj["Description"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.BinType:str = obj["BinType"]
      """   Valid values: "Std,Cust, Supp, Cont".
Std - Standard, Cust - Customer owned, Supp - Supplier Owned, Cont - Planning Contract.  """  
      self.Replenishable:bool = obj["Replenishable"]
      """  Replenishable  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.Description:str = obj["Description"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.NonNettable:bool = obj["NonNettable"]
      """  Indicates if the quantity of the warehouse bin should be considered towards the available quantity of the part.  """  
      self.SizeID:str = obj["SizeID"]
      """  The SizeID is the reference to the BinSize record which defines the physical size. Optional, but if entered must be valid.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  The ZoneID is the reference to the WhseZone record. Optional, but if entered must be valid.  """  
      self.BinSeq:int = obj["BinSeq"]
      """  allows the warhhouse manager to assing sequences to Bins used during the picking process. The pick ticked can be sorted in Bin Sequence ordr allowing the picker to traverse thru an aisle systematically. Also allows the Queue transactions to be sorted systematically.  """  
      self.BinType:str = obj["BinType"]
      """   Valid values: "Std,Cust, Supp, Cont".
Std - Standard, Cust - Customer owned, Supp - Supplier Owned, Cont - Planning Contract.  """  
      self.CustNum:int = obj["CustNum"]
      """  For BinType = Cust, this is the Customer number of the Customer that owns the contents stored in this bin. If BinType = "Cust" then must be a valid Customer reference.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  For BinType = Supl, this is the Supplier (vendor) number of the Supplier that owns the contents stored in this bin. If BinType = "Supl" then must be a valid Vendor reference.  """  
      self.Aisle:str = obj["Aisle"]
      """  Optional, used to specify the aisle that the bin is located in. Disable if Portable = true  """  
      self.Face:str = obj["Face"]
      """  Optional, used to specify the face within the aisle that the bin is located on. Disable if Portable = true  """  
      self.Elevation:int = obj["Elevation"]
      """  Optional. Used to specify the elevation of the bin. Normally the bin on the gound level would be 1, the bin above that would be 2, and so on.  """  
      self.MaxFill:int = obj["MaxFill"]
      """  Maximum Fill  """  
      self.PctFillable:int = obj["PctFillable"]
      """  Percentage Fillable  """  
      self.InActive:bool = obj["InActive"]
      """  Can only be set to True if the bin is empty. If inactive, then is should not be valid in any future transactions.  """  
      self.Portable:bool = obj["Portable"]
      """  Indicates if the bin is not in a fixed location.  """  
      self.Replenishable:bool = obj["Replenishable"]
      """  Replenishable  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the warehouse bin has to be synchronized with Epicor FSA application.  """  
      self.AttrBinList:str = obj["AttrBinList"]
      """  Delimited list of Warehouse Bin Attributes  """  
      self.IsEmpty:bool = obj["IsEmpty"]
      """  Used to prevent change of BinType if bin has OnhandQty.  """  
      self.PlantSendToFSA:bool = obj["PlantSendToFSA"]
      """  Determines if the plant (retrieved from parent warehouse) has to be synchronized with Epicor FSA application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.SizeIDDescription:str = obj["SizeIDDescription"]
      self.VendorName:str = obj["VendorName"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.WarehouseCodePlant:str = obj["WarehouseCodePlant"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.ZoneIDZoneDesc:str = obj["ZoneIDZoneDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddNewWhseBinFormat_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class AddNewWhseBinFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CommitGeneratedBins_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class CommitGeneratedBins_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   warehouseCode
   binNum
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtWhseBinTableset:
   def __init__(self, obj):
      self.WhseBin:list[Erp_Tablesets_WhseBinRow] = obj["WhseBin"]
      self.WhseBinAttch:list[Erp_Tablesets_WhseBinAttchRow] = obj["WhseBinAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhseBinAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
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

class Erp_Tablesets_WhseBinFormatRow:
   def __init__(self, obj):
      self.Seq:int = obj["Seq"]
      """  Sequence of the Segment  """  
      self.Type:str = obj["Type"]
      """  Segment type  """  
      self.Positions:int = obj["Positions"]
      """  Number of digits in the segment  """  
      self.Minimum:str = obj["Minimum"]
      """  Lowest value allowed for the segment  """  
      self.Maximum:str = obj["Maximum"]
      """  Top value that the segment can have  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseBinListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.Description:str = obj["Description"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.BinType:str = obj["BinType"]
      """   Valid values: "Std,Cust, Supp, Cont".
Std - Standard, Cust - Customer owned, Supp - Supplier Owned, Cont - Planning Contract.  """  
      self.Replenishable:bool = obj["Replenishable"]
      """  Replenishable  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseBinListTableset:
   def __init__(self, obj):
      self.WhseBinList:list[Erp_Tablesets_WhseBinListRow] = obj["WhseBinList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhseBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.Description:str = obj["Description"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.NonNettable:bool = obj["NonNettable"]
      """  Indicates if the quantity of the warehouse bin should be considered towards the available quantity of the part.  """  
      self.SizeID:str = obj["SizeID"]
      """  The SizeID is the reference to the BinSize record which defines the physical size. Optional, but if entered must be valid.  """  
      self.ZoneID:str = obj["ZoneID"]
      """  The ZoneID is the reference to the WhseZone record. Optional, but if entered must be valid.  """  
      self.BinSeq:int = obj["BinSeq"]
      """  allows the warhhouse manager to assing sequences to Bins used during the picking process. The pick ticked can be sorted in Bin Sequence ordr allowing the picker to traverse thru an aisle systematically. Also allows the Queue transactions to be sorted systematically.  """  
      self.BinType:str = obj["BinType"]
      """   Valid values: "Std,Cust, Supp, Cont".
Std - Standard, Cust - Customer owned, Supp - Supplier Owned, Cont - Planning Contract.  """  
      self.CustNum:int = obj["CustNum"]
      """  For BinType = Cust, this is the Customer number of the Customer that owns the contents stored in this bin. If BinType = "Cust" then must be a valid Customer reference.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  For BinType = Supl, this is the Supplier (vendor) number of the Supplier that owns the contents stored in this bin. If BinType = "Supl" then must be a valid Vendor reference.  """  
      self.Aisle:str = obj["Aisle"]
      """  Optional, used to specify the aisle that the bin is located in. Disable if Portable = true  """  
      self.Face:str = obj["Face"]
      """  Optional, used to specify the face within the aisle that the bin is located on. Disable if Portable = true  """  
      self.Elevation:int = obj["Elevation"]
      """  Optional. Used to specify the elevation of the bin. Normally the bin on the gound level would be 1, the bin above that would be 2, and so on.  """  
      self.MaxFill:int = obj["MaxFill"]
      """  Maximum Fill  """  
      self.PctFillable:int = obj["PctFillable"]
      """  Percentage Fillable  """  
      self.InActive:bool = obj["InActive"]
      """  Can only be set to True if the bin is empty. If inactive, then is should not be valid in any future transactions.  """  
      self.Portable:bool = obj["Portable"]
      """  Indicates if the bin is not in a fixed location.  """  
      self.Replenishable:bool = obj["Replenishable"]
      """  Replenishable  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the warehouse bin has to be synchronized with Epicor FSA application.  """  
      self.AttrBinList:str = obj["AttrBinList"]
      """  Delimited list of Warehouse Bin Attributes  """  
      self.IsEmpty:bool = obj["IsEmpty"]
      """  Used to prevent change of BinType if bin has OnhandQty.  """  
      self.PlantSendToFSA:bool = obj["PlantSendToFSA"]
      """  Determines if the plant (retrieved from parent warehouse) has to be synchronized with Epicor FSA application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.CustomerInactive:bool = obj["CustomerInactive"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.SizeIDDescription:str = obj["SizeIDDescription"]
      self.VendorName:str = obj["VendorName"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.WarehouseCodePlant:str = obj["WarehouseCodePlant"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.ZoneIDZoneDesc:str = obj["ZoneIDZoneDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseBinTableset:
   def __init__(self, obj):
      self.WhseBin:list[Erp_Tablesets_WhseBinRow] = obj["WhseBin"]
      self.WhseBinAttch:list[Erp_Tablesets_WhseBinAttchRow] = obj["WhseBinAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhseBinWizardRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company where the Bin belongs  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Wharehouse where the Bin belongs  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin Number  """  
      self.Description:str = obj["Description"]
      """  Bin Description  """  
      self.ZoneId:str = obj["ZoneId"]
      """  Zone Id  """  
      self.SizeID:str = obj["SizeID"]
      """  Size Id  """  
      self.BinSeq:int = obj["BinSeq"]
      """  Bin Sequence  """  
      self.BinType:str = obj["BinType"]
      """  Bin Type  """  
      self.MaxFill:int = obj["MaxFill"]
      """  Max Fill  """  
      self.PctFillable:int = obj["PctFillable"]
      """  Percentage Fillable  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.NonNettable:bool = obj["NonNettable"]
      """  Non Nettable  """  
      self.Portable:bool = obj["Portable"]
      """  Portable  """  
      self.Replenishable:bool = obj["Replenishable"]
      """  Replenishable  """  
      self.Aisle:str = obj["Aisle"]
      """  Aisle  """  
      self.Face:str = obj["Face"]
      """  Face  """  
      self.Elevation:int = obj["Elevation"]
      """  Elevation  """  
      self.BinNumFormat:str = obj["BinNumFormat"]
      """  Bin Numbers Format  """  
      self.Selected:bool = obj["Selected"]
      """  True when the Bin Number is selected  """  
      self.Exist:bool = obj["Exist"]
      """  True when the Bin Number already exists  """  
      self.AutoSeq:bool = obj["AutoSeq"]
      """  True when sequence will automatically increased  """  
      self.WhseDescription:str = obj["WhseDescription"]
      """  Warehouse description  """  
      self.ZoneDescription:str = obj["ZoneDescription"]
      """  Zone Description  """  
      self.SizeDescription:str = obj["SizeDescription"]
      """  Bin Size description  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.CustomerName:str = obj["CustomerName"]
      self.VendorID:str = obj["VendorID"]
      """  VendorID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.VendorName:str = obj["VendorName"]
      """  VendorName  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the warehouse bin has to be synchronized with Epicor FSA application.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhseBinWizardTableset:
   def __init__(self, obj):
      self.WhseBinFormat:list[Erp_Tablesets_WhseBinFormatRow] = obj["WhseBinFormat"]
      self.WhseBinWizard:list[Erp_Tablesets_WhseBinWizardRow] = obj["WhseBinWizard"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateBinFormat_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class GenerateBinFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateBins_input:
   """ Required : 
   totalBins
   ds
   """  
   def __init__(self, obj):
      self.totalBins:int = obj["totalBins"]
      """  Number of Bin Numbers to be generated  """  
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class GenerateBins_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   warehouseCode
   binNum
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhseBinTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WhseBinTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WhseBinTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WhseBinListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewWhseBinAttch_input:
   """ Required : 
   ds
   warehouseCode
   binNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      pass

class GetNewWhseBinAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhseBin_input:
   """ Required : 
   ds
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewWhseBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseWhseBin
   whereClauseWhseBinAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseWhseBin:str = obj["whereClauseWhseBin"]
      self.whereClauseWhseBinAttch:str = obj["whereClauseWhseBinAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WhseBinTableset] = obj["returnObj"]
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

class InActiveFlag_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeCustID_input:
   """ Required : 
   newCustID
   ds
   """  
   def __init__(self, obj):
      self.newCustID:str = obj["newCustID"]
      """  Customer.CustID  """  
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      pass

class OnChangeCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSuppID_input:
   """ Required : 
   newVendorID
   ds
   """  
   def __init__(self, obj):
      self.newVendorID:str = obj["newVendorID"]
      """  Vendor.VendorID  """  
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      pass

class OnChangeSuppID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWhseBinWizardCustId_input:
   """ Required : 
   newCustID
   ds
   """  
   def __init__(self, obj):
      self.newCustID:str = obj["newCustID"]
      """  Customer.CustID  """  
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class OnChangeWhseBinWizardCustId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWhseBinWizardSuppId_input:
   """ Required : 
   newVendorID
   ds
   """  
   def __init__(self, obj):
      self.newVendorID:str = obj["newVendorID"]
      """  Vendor.VendorID  """  
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class OnChangeWhseBinWizardSuppId_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSegmentMaximum_input:
   """ Required : 
   iSegment
   newValue
   ds
   """  
   def __init__(self, obj):
      self.iSegment:int = obj["iSegment"]
      """  Segment that is being modified  """  
      self.newValue:str = obj["newValue"]
      """  New Maximum value  """  
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class OnChangingSegmentMaximum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSegmentMinimum_input:
   """ Required : 
   iSegment
   newValue
   ds
   """  
   def __init__(self, obj):
      self.iSegment:int = obj["iSegment"]
      """  Segment that is being modified  """  
      self.newValue:str = obj["newValue"]
      """  New Minimum value  """  
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class OnChangingSegmentMinimum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSegmentPositions_input:
   """ Required : 
   iSegment
   newValue
   ds
   """  
   def __init__(self, obj):
      self.iSegment:int = obj["iSegment"]
      """  Segment that is being modified  """  
      self.newValue:int = obj["newValue"]
      """  New Positions value  """  
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class OnChangingSegmentPositions_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSegmentType_input:
   """ Required : 
   iSegment
   newValue
   ds
   """  
   def __init__(self, obj):
      self.iSegment:int = obj["iSegment"]
      """  Segment that is being modified  """  
      self.newValue:str = obj["newValue"]
      """  New Type value  """  
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

class OnChangingSegmentType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinWizardTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWhseBinTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWhseBinTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WhseBinTableset] = obj["ds"]
      pass

      """  output parameters  """  

