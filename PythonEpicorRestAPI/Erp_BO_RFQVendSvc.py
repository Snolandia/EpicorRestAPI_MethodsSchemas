import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RFQVendSvc
# Description: Purchase Request For Quote Vendor
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RFQVends(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQVends
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends",headers=creds) as resp:
           return await resp.json()

async def post_RFQVends(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQVend item
   Description: Calls GetByID to retrieve the RFQVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQVend for the service
   Description: Calls UpdateExt to update RFQVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQVends_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQVend item
   Description: Call UpdateExt to delete RFQVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQVends(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def get_RFQLinesSelecteds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RFQLinesSelecteds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RFQLinesSelecteds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQLinesSelectedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds",headers=creds) as resp:
           return await resp.json()

async def post_RFQLinesSelecteds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RFQLinesSelecteds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RFQLinesSelectedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RFQLinesSelectedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RFQLinesSelecteds_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RFQLinesSelected item
   Description: Calls GetByID to retrieve the RFQLinesSelected item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RFQLinesSelected
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RFQLinesSelectedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RFQLinesSelecteds_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RFQLinesSelected for the service
   Description: Calls UpdateExt to update RFQLinesSelected. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RFQLinesSelected
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RFQLinesSelectedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RFQLinesSelecteds_Company_RFQNum_RFQLine_VendorNum_PurPoint(Company, RFQNum, RFQLine, VendorNum, PurPoint, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RFQLinesSelected item
   Description: Call UpdateExt to delete RFQLinesSelected item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RFQLinesSelected
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RFQNum: Desc: RFQNum   Required: True
      :param RFQLine: Desc: RFQLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/RFQLinesSelecteds(" + Company + "," + RFQNum + "," + RFQLine + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RFQVendListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRFQVend, whereClauseRFQLinesSelected, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRFQVend=" + whereClauseRFQVend
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRFQLinesSelected=" + whereClauseRFQLinesSelected
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rfQNum, rfQLine, vendorNum, purPoint, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
   Required: True
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
   params += "rfQNum=" + rfQNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rfQLine=" + rfQLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "purPoint=" + purPoint

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AvailableResponses(epicorHeaders = None):
   """  
   Summary: Invoke method AvailableResponses
   Description: Return list of available responses.
   OperationID: AvailableResponses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AvailableResponses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailCalcOurQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailCalcOurQty
   Description: Run this method when our quantity on the detail changes.
   OperationID: ChangeDetailCalcOurQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCalcOurQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCalcOurQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailCalcVendQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailCalcVendQty
   Description: Run this method when supplier quantity on the detail changes.
   OperationID: ChangeDetailCalcVendQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailCalcVendQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailCalcVendQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPOCreation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPOCreation
   Description: This method checks if everything is okay before creating a PO. If there are
any questions to be asked they will be returned in the 2 message parameters.
If the user answers yes to both questions, then CreatePO can be run
   OperationID: CheckPOCreation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPOCreation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPOCreation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreatePO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreatePO
   Description: This method Creates a PO for the current RFQVend Line.  If a PO is above a person's
approval limit, then the PO will be created but not approved
   OperationID: CreatePO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreatePO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillRFQLinesSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillRFQLinesSelected
   Description: Run this method to Fill RFQLinesSelected Temp Table with records selected to Create PO
   OperationID: FillRFQLinesSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillRFQLinesSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillRFQLinesSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLineQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLineQty
   Description: This method gets the Job Qty (if job related) and sets a flag to tell the UI
to update the Qty, duedate and promise date fields
   OperationID: GetLineQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLineQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLineQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method to allow sort by external columns
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRFQsForSupplierTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRFQsForSupplierTracker
   Description: Called from Supplier tracker instead of RFQVend GetRows
   OperationID: GetRFQsForSupplierTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRFQsForSupplierTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRFQsForSupplierTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ListOfRFQVend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ListOfRFQVend
   Description: This is a copy of GetList modified to have the RFQ Source and RFQ Status search values  be passed as  parameters
instead of being in the where clause. Run This instead of GetList.
UI - DO NOT include 'RFQ source' and 'RFQ status' in the where clause. Instead, pass them as parameters per the following:
   OperationID: ListOfRFQVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ListOfRFQVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListOfRFQVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ListOfRFQVendWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ListOfRFQVendWhereClause
   Description: This is a copy of ListOfRFQVend modified to accept an RFQNum as a parameter and fill the list filtered by that RFQNum.
   OperationID: ListOfRFQVendWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ListOfRFQVendWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListOfRFQVendWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ListOfRFQVendWhereClauseVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ListOfRFQVendWhereClauseVendor
   Description: This is a copy of ListOfRFQVend modified to accept an RFQNum as a parameter and fill the list filtered by that RFQNum.
   OperationID: ListOfRFQVendWhereClauseVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ListOfRFQVendWhereClauseVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ListOfRFQVendWhereClauseVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshDataset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshDataset
   Description: This method does refresh for each loaded records.
   OperationID: RefreshDataset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RowsOfRFQVend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RowsOfRFQVend
   Description: This is a copy of GetRows modified to have the RFQ Source and RFQ Status search values  be passed as  parameters
instead of being in the where clause. can be run instead of GetRows.
UI - DO NOT include 'RFQ source' and 'RFQ status' in the where clause. Instead, pass them as parameters per the following:
            
            
<returns>Returns RFQVendDataSet data set.</returns><param name="whereClause">Where clause to filter the query results.</param><param name="pageSize">page size.</param><param name="absolutePage">absolute page</param><param name="morePages">more pages.</param><param name="rfqSourcein">If 'all'  -> input 'A', if 'jobs' -> input 'J',  if 'Quotes' -> input 'Q'.</param><param name="rfqStatusin">If 'all'  -> input 'A', if 'closed' -> input 'C', if 'open' -> input 'O'. </param>
   OperationID: RowsOfRFQVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RowsOfRFQVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RowsOfRFQVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRFQVend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRFQVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRFQVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRFQVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRFQVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RFQVendSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQLinesSelectedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQLinesSelectedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQVendListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RFQVendRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RFQVendRow] = obj["value"]
      pass

class Erp_Tablesets_RFQLinesSelectedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RFQNum:int = obj["RFQNum"]
      self.RFQLine:int = obj["RFQLine"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PartNum:str = obj["PartNum"]
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.IUM:str = obj["IUM"]
      self.LineDescription:str = obj["LineDescription"]
      self.OurUOM:str = obj["OurUOM"]
      self.PUM:str = obj["PUM"]
      self.DueDate:str = obj["DueDate"]
      self.PromiseDate:str = obj["PromiseDate"]
      self.EnableOurQty:bool = obj["EnableOurQty"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeShortDescription:str = obj["AttributeShortDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQVendListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenItem:bool = obj["OpenItem"]
      """  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  """  
      self.Response:str = obj["Response"]
      """   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number  that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point ID.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this RFQ  """  
      self.RespondVia:str = obj["RespondVia"]
      """  Can be "Web" or "Client"  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Compliance Message  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.OpenRFQ:bool = obj["OpenRFQ"]
      self.LineDescription:str = obj["LineDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.JobNum:str = obj["JobNum"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.OpCode:str = obj["OpCode"]
      self.OpDescription:str = obj["OpDescription"]
      self.ResponseDescription:str = obj["ResponseDescription"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Vend Part Effective Date  """  
      self.RFQSource:str = obj["RFQSource"]
      """  Description of the Source field (either Job, Quote or blank)  """  
      self.RFQStatus:str = obj["RFQStatus"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer Name  """  
      self.RFQDate:str = obj["RFQDate"]
      self.RFQDueDate:str = obj["RFQDueDate"]
      self.OurUOM:str = obj["OurUOM"]
      """  Our UOM  """  
      self.SupplierUOM:str = obj["SupplierUOM"]
      """  Supplier UOM  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM Code from Part Master  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.AttributeShortDescription:str = obj["AttributeShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenItem:bool = obj["OpenItem"]
      """  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  """  
      self.Response:str = obj["Response"]
      """   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number  that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point ID.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this RFQ  """  
      self.RespondVia:str = obj["RespondVia"]
      """  Can be "Web" or "Client"  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Compliance Message  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.OpenRFQ:bool = obj["OpenRFQ"]
      self.LineDescription:str = obj["LineDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.JobNum:str = obj["JobNum"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.OpCode:str = obj["OpCode"]
      self.OpDescription:str = obj["OpDescription"]
      self.ResponseDescription:str = obj["ResponseDescription"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Vend Part Effective Date  """  
      self.RFQSource:str = obj["RFQSource"]
      """  Description of the Source field (either Job, Quote or blank)  """  
      self.RFQStatus:str = obj["RFQStatus"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer Name  """  
      self.RFQDate:str = obj["RFQDate"]
      self.RFQDueDate:str = obj["RFQDueDate"]
      self.OurUOM:str = obj["OurUOM"]
      """  Our UOM  """  
      self.SupplierUOM:str = obj["SupplierUOM"]
      """  Supplier UOM  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM Code from Part Master  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.Selected:bool = obj["Selected"]
      self.AddressFormatted:str = obj["AddressFormatted"]
      """  Supplier Address  """  
      self.ResponseOptions:str = obj["ResponseOptions"]
      """  Valid Response options for combo.  """  
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeShortDescription:str = obj["AttributeShortDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AvailableResponses_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.responseList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeDetailCalcOurQty_input:
   """ Required : 
   NewCalcOurQty
   ds
   """  
   def __init__(self, obj):
      self.NewCalcOurQty:int = obj["NewCalcOurQty"]
      """  New Quantity  """  
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

class ChangeDetailCalcOurQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDetailCalcVendQty_input:
   """ Required : 
   NewCalcVendQty
   ds
   """  
   def __init__(self, obj):
      self.NewCalcVendQty:int = obj["NewCalcVendQty"]
      """  New Quantity  """  
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

class ChangeDetailCalcVendQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPOCreation_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

class CheckPOCreation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      self.vendMessage:str = obj["parameters"]
      self.vWarningMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreatePO_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

class CreatePO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msgString:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rfQNum
   rfQLine
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.rfQNum:int = obj["rfQNum"]
      self.rfQLine:int = obj["rfQLine"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_RFQLinesSelectedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RFQNum:int = obj["RFQNum"]
      self.RFQLine:int = obj["RFQLine"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.PartNum:str = obj["PartNum"]
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.IUM:str = obj["IUM"]
      self.LineDescription:str = obj["LineDescription"]
      self.OurUOM:str = obj["OurUOM"]
      self.PUM:str = obj["PUM"]
      self.DueDate:str = obj["DueDate"]
      self.PromiseDate:str = obj["PromiseDate"]
      self.EnableOurQty:bool = obj["EnableOurQty"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeShortDescription:str = obj["AttributeShortDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQVendListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenItem:bool = obj["OpenItem"]
      """  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  """  
      self.Response:str = obj["Response"]
      """   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number  that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point ID.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this RFQ  """  
      self.RespondVia:str = obj["RespondVia"]
      """  Can be "Web" or "Client"  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Compliance Message  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.OpenRFQ:bool = obj["OpenRFQ"]
      self.LineDescription:str = obj["LineDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.JobNum:str = obj["JobNum"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.OpCode:str = obj["OpCode"]
      self.OpDescription:str = obj["OpDescription"]
      self.ResponseDescription:str = obj["ResponseDescription"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Vend Part Effective Date  """  
      self.RFQSource:str = obj["RFQSource"]
      """  Description of the Source field (either Job, Quote or blank)  """  
      self.RFQStatus:str = obj["RFQStatus"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer Name  """  
      self.RFQDate:str = obj["RFQDate"]
      self.RFQDueDate:str = obj["RFQDueDate"]
      self.OurUOM:str = obj["OurUOM"]
      """  Our UOM  """  
      self.SupplierUOM:str = obj["SupplierUOM"]
      """  Supplier UOM  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM Code from Part Master  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      """   Description of line item.
Defaults from JobOper, JobMtl or Part depending on the reference.  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.AttributeShortDescription:str = obj["AttributeShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQVendListTableset:
   def __init__(self, obj):
      self.RFQVendList:list[Erp_Tablesets_RFQVendListRow] = obj["RFQVendList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RFQVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenItem:bool = obj["OpenItem"]
      """  Indicates if this line item is Open/Closed. Gets set to "Closed" when there are no longer any open RFQDtl records. This can also be closed when the user voids the RFQItem.  """  
      self.Response:str = obj["Response"]
      """   Indicates if the vendor has responded. This field is not directly maintainable, when price breaks are entered this is set to yes.
Valid values are 
 "W" = WAITING for response,
 "R" = response RECEIVED, and
 "N" = NO response RECEIVED, nor are we waiting for one.  """  
      self.RFQNum:int = obj["RFQNum"]
      """  RFQ number  that the item is linked to.  """  
      self.RFQLine:int = obj["RFQLine"]
      """  The line number of the detail record on the RFQ. This number uniquely identifies the record within the RFQ. The number is not directly maintainable, it's assigned by the system when records are created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor's unique internal number.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point ID.  """  
      self.ConNum:int = obj["ConNum"]
      """  Supplier contact linked to this RFQ  """  
      self.RespondVia:str = obj["RespondVia"]
      """  Can be "Web" or "Client"  """  
      self.RespondDate:str = obj["RespondDate"]
      """  Date Supplier responded to the RFQ.  Only used when the response came from the Web.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Compliance Message  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorID:str = obj["VendorID"]
      self.VendorName:str = obj["VendorName"]
      self.OpenRFQ:bool = obj["OpenRFQ"]
      self.LineDescription:str = obj["LineDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.JobNum:str = obj["JobNum"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.OpCode:str = obj["OpCode"]
      self.OpDescription:str = obj["OpDescription"]
      self.ResponseDescription:str = obj["ResponseDescription"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Vend Part Effective Date  """  
      self.RFQSource:str = obj["RFQSource"]
      """  Description of the Source field (either Job, Quote or blank)  """  
      self.RFQStatus:str = obj["RFQStatus"]
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer Name  """  
      self.RFQDate:str = obj["RFQDate"]
      self.RFQDueDate:str = obj["RFQDueDate"]
      self.OurUOM:str = obj["OurUOM"]
      """  Our UOM  """  
      self.SupplierUOM:str = obj["SupplierUOM"]
      """  Supplier UOM  """  
      self.IUM:str = obj["IUM"]
      """  Base UOM Code from Part Master  """  
      self.PUM:str = obj["PUM"]
      """  The Purchasing Unit of measure for the Part.  """  
      self.CalcOurQty:int = obj["CalcOurQty"]
      self.CalcVendQty:int = obj["CalcVendQty"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source.  """  
      self.Selected:bool = obj["Selected"]
      self.AddressFormatted:str = obj["AddressFormatted"]
      """  Supplier Address  """  
      self.ResponseOptions:str = obj["ResponseOptions"]
      """  Valid Response options for combo.  """  
      self.AttributeDescription:str = obj["AttributeDescription"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeShortDescription:str = obj["AttributeShortDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RFQLineLineDesc:str = obj["RFQLineLineDesc"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RFQVendTableset:
   def __init__(self, obj):
      self.RFQVend:list[Erp_Tablesets_RFQVendRow] = obj["RFQVend"]
      self.RFQLinesSelected:list[Erp_Tablesets_RFQLinesSelectedRow] = obj["RFQLinesSelected"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRFQVendTableset:
   def __init__(self, obj):
      self.RFQVend:list[Erp_Tablesets_RFQVendRow] = obj["RFQVend"]
      self.RFQLinesSelected:list[Erp_Tablesets_RFQLinesSelectedRow] = obj["RFQLinesSelected"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FillRFQLinesSelected_input:
   """ Required : 
   strRowsSelected
   ds
   """  
   def __init__(self, obj):
      self.strRowsSelected:str = obj["strRowsSelected"]
      """  A RowId list of selected RFQVend records.  """  
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

class FillRFQLinesSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   rfQNum
   rfQLine
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.rfQNum:int = obj["rfQNum"]
      self.rfQLine:int = obj["rfQLine"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQVendTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQVendTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQVendTableset] = obj["returnObj"]
      pass

class GetLineQty_input:
   """ Required : 
   rfqNum
   rfqLine
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.rfqNum:int = obj["rfqNum"]
      """  RFQ Number  """  
      self.rfqLine:int = obj["rfqLine"]
      """  RFQ Line Number  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.purPoint:str = obj["purPoint"]
      """  Vendor Purchase Point  """  
      pass

class GetLineQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.tmpLineQty:int = obj["parameters"]
      self.promptQty:bool = obj["promptQty"]
      pass

      """  output parameters  """  

class GetListCustom_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause for RFQVend table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQVendListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RFQVendListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRFQVend_input:
   """ Required : 
   ds
   rfQNum
   rfQLine
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      self.rfQNum:int = obj["rfQNum"]
      self.rfQLine:int = obj["rfQLine"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewRFQVend_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRFQsForSupplierTracker_input:
   """ Required : 
   company
   vendN
   dateRange
   openItem
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  Current company.  """  
      self.vendN:int = obj["vendN"]
      """  Current vendor number.  """  
      self.dateRange:str = obj["dateRange"]
      """  Current Transaction Date Range.  """  
      self.openItem:str = obj["openItem"]
      """  Current tab selected: All / Open / Closed.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRFQsForSupplierTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQVendTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRFQVend
   whereClauseRFQLinesSelected
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRFQVend:str = obj["whereClauseRFQVend"]
      self.whereClauseRFQLinesSelected:str = obj["whereClauseRFQLinesSelected"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQVendTableset] = obj["returnObj"]
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

class ListOfRFQVendWhereClauseVendor_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   rfqSourcein
   rfqStatusin
   rfqNum
   vendorId
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The full where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      self.rfqSourcein:str = obj["rfqSourcein"]
      """  If 'all'  -> input 'A', if 'jobs' -> input 'J',  if 'Quotes' -> input 'Q'.  """  
      self.rfqStatusin:str = obj["rfqStatusin"]
      """  If "all'  -> input 'A', if 'closed' -> input 'C', if "open" -> input 'O'.  """  
      self.rfqNum:int = obj["rfqNum"]
      """  The RFQ to filter the list by  """  
      self.vendorId:str = obj["vendorId"]
      pass

class ListOfRFQVendWhereClauseVendor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQVendListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class ListOfRFQVendWhereClause_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   rfqSourcein
   rfqStatusin
   rfqNum
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The full where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      self.rfqSourcein:str = obj["rfqSourcein"]
      """  If 'all'  -> input 'A', if 'jobs' -> input 'J',  if 'Quotes' -> input 'Q'.  """  
      self.rfqStatusin:str = obj["rfqStatusin"]
      """  If "all'  -> input 'A', if 'closed' -> input 'C', if "open" -> input 'O'.  """  
      self.rfqNum:int = obj["rfqNum"]
      """  The RFQ to filter the list by  """  
      pass

class ListOfRFQVendWhereClause_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQVendListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class ListOfRFQVend_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   rfqSourcein
   rfqStatusin
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause to filter the query results.  """  
      self.pageSize:int = obj["pageSize"]
      """  page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolute page  """  
      self.rfqSourcein:str = obj["rfqSourcein"]
      """  If 'all'  -> input 'A', if 'jobs' -> input 'J',  if 'Quotes' -> input 'Q'.  """  
      self.rfqStatusin:str = obj["rfqStatusin"]
      """  If "all'  -> input 'A', if 'closed' -> input 'C', if "open" -> input 'O'.  """  
      pass

class ListOfRFQVend_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQVendListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class RefreshDataset_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

class RefreshDataset_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RowsOfRFQVend_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   rfqSourcein
   rfqStatusin
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      self.rfqSourcein:str = obj["rfqSourcein"]
      self.rfqStatusin:str = obj["rfqStatusin"]
      pass

class RowsOfRFQVend_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RFQVendTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRFQVendTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRFQVendTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RFQVendTableset] = obj["ds"]
      pass

      """  output parameters  """  

