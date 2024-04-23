import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ForecastSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Forecasts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Forecasts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Forecasts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ForecastRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts",headers=creds) as resp:
           return await resp.json()

async def post_Forecasts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Forecasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ForecastRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ForecastRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum(Company, PartNum, Plant, CustNum, ForeDate, AttributeSetID, ParentPartNum, ShipToNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Forecast item
   Description: Calls GetByID to retrieve the Forecast item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Forecast
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ForecastRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum(Company, PartNum, Plant, CustNum, ForeDate, AttributeSetID, ParentPartNum, ShipToNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Forecast for the service
   Description: Calls UpdateExt to update Forecast. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Forecast
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ForecastRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum(Company, PartNum, Plant, CustNum, ForeDate, AttributeSetID, ParentPartNum, ShipToNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Forecast item
   Description: Call UpdateExt to delete Forecast item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Forecast
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_ForecastAttches(Company, PartNum, Plant, CustNum, ForeDate, AttributeSetID, ParentPartNum, ShipToNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ForecastAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ForecastAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ForecastAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")/ForecastAttches",headers=creds) as resp:
           return await resp.json()

async def get_Forecasts_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_ForecastAttches_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_DrawingSeq(Company, PartNum, Plant, CustNum, ForeDate, AttributeSetID, ParentPartNum, ShipToNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ForecastAttch item
   Description: Calls GetByID to retrieve the ForecastAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ForecastAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ForecastAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/Forecasts(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + ")/ForecastAttches(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ForecastAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ForecastAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ForecastAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ForecastAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches",headers=creds) as resp:
           return await resp.json()

async def post_ForecastAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ForecastAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ForecastAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ForecastAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ForecastAttches_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_DrawingSeq(Company, PartNum, Plant, CustNum, ForeDate, AttributeSetID, ParentPartNum, ShipToNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ForecastAttch item
   Description: Calls GetByID to retrieve the ForecastAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ForecastAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ForecastAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ForecastAttches_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_DrawingSeq(Company, PartNum, Plant, CustNum, ForeDate, AttributeSetID, ParentPartNum, ShipToNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ForecastAttch for the service
   Description: Calls UpdateExt to update ForecastAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ForecastAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ForecastAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ForecastAttches_Company_PartNum_Plant_CustNum_ForeDate_AttributeSetID_ParentPartNum_ShipToNum_DrawingSeq(Company, PartNum, Plant, CustNum, ForeDate, AttributeSetID, ParentPartNum, ShipToNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ForecastAttch item
   Description: Call UpdateExt to delete ForecastAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ForecastAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ForeDate: Desc: ForeDate   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param ParentPartNum: Desc: ParentPartNum   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/ForecastAttches(" + Company + "," + PartNum + "," + Plant + "," + CustNum + "," + ForeDate + "," + AttributeSetID + "," + ParentPartNum + "," + ShipToNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ForecastListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseForecast, whereClauseForecastAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseForecast=" + whereClauseForecast
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseForecastAttch=" + whereClauseForecastAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, plant, custNum, foreDate, attributeSetID, parentPartNum, shipToNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "custNum=" + custNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "foreDate=" + foreDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "attributeSetID=" + attributeSetID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "parentPartNum=" + parentPartNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "shipToNum=" + shipToNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ClearForecasts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearForecasts
   Description: This method deletes all Forecast records for the Current Plant, or all Plants, with two exceptions:
- Forecasts for Global Parts are not deleted
- Forecasts marked as autoTransfer are not deleted.
   OperationID: ClearForecasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearShipToForecasts(epicorHeaders = None):
   """  
   Summary: Invoke method ClearShipToForecasts
   Description: This method removes the ShipToNum from all the Forecasts
   OperationID: ClearShipToForecasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearShipToForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangingShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingShipTo
   Description: Validate the ShipTo Id.
   OperationID: OnChangingShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportForecasts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportForecasts
   Description: This method exports all Forecast records for the current company, after the given date.
            
If ForecastImportExport records are present as input, they are used to build the following
lists for selection of records:
PlantList
PartList
CustNumList
If a record in the input dataset:
1) has a value for Plant, PartNum, or CustID and blank values for the other two, and
2) blank values for the fields ImportErrorMsg and ForeQty,
then the value in Plant, PartNum, or CustID will be added to the respective
list.
If a record has a value in more than one of these fields, it will be ignored.
            
After the above lists have been constructed, the record selection will use the lists as follows:
- if a list is non-empty, only records whose corresponding field value appears in the list
will be a candidate for being included in the returned dataset, subject to the other conditions
- if a list is empty, no filtering will occur on the values for that field, except possibly
conditions in the "whereClauseForecast" parameter.
   OperationID: ExportForecasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertForecastsToCSV(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertForecastsToCSV
   Description: This method receives a ForecastImportExportTableset and returns a CSV file to export
   OperationID: ConvertForecastsToCSV
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertForecastsToCSV_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertForecastsToCSV_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportForecastsReadFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportForecastsReadFile
   Description: This methods receives a CSV file Path and imports the Forecasts found
   OperationID: ImportForecastsReadFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportForecastsReadFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportForecastsReadFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNextDateNewForecast(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNextDateNewForecast
   Description: Calculates the next ForeDate from the Forecast selected before the GetNew operation
   OperationID: GetNextDateNewForecast
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNextDateNewForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextDateNewForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetForecastDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetForecastDays
   Description: To retrieve the ForecastDaysBefore and ForecastDaysAfter from the JC system settings.
   OperationID: GetForecastDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetForecastDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetForecastDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewForecastImportExport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewForecastImportExport
   Description: This method creates a new ForecastImportExport dataset row.
   OperationID: GetNewForecastImportExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewForecastImportExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForecastImportExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSalesHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSalesHistory
   Description: This method provides a ForecastSalesHistory dataset filled with Sales History data.  This can
be used as the basis of the External Forecast Export.
            
Notes:      taken from mre10-sm-ex-dg.w (PROCEDURE Export-Forecast)
   OperationID: GetSalesHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSalesHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSalesHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportExternalForecast(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportExternalForecast
   Description: This method populates the ttForecastImportExport dataset with forecast data.
   OperationID: ImportExternalForecast
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportExternalForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportExternalForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportForecasts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportForecasts
   Description: This method conditionally adds/overwrites Forecast records using the same logic as
the Vantage Forecast Import screen.
   OperationID: ImportForecasts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsConfigurable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsConfigurable
   OperationID: IsConfigurable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsConfigurable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsConfigurable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAttributeSetIDFromRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewForecast(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewForecast
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewForecast
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewForecastAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewForecastAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewForecastAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewForecastAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewForecastAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ForecastSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ForecastAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ForecastListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ForecastRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ForecastRow] = obj["value"]
      pass

class Erp_Tablesets_ForecastAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.CustNum:int = obj["CustNum"]
      self.ForeDate:str = obj["ForeDate"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      self.ShipToNum:str = obj["ShipToNum"]
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

class Erp_Tablesets_ForecastListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this forecast  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.ForeQty:int = obj["ForeQty"]
      """  Forecast quantity  """  
      self.ForeQtyUOM:str = obj["ForeQtyUOM"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.PONum:str = obj["PONum"]
      """  Inbound Customer PO Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date the forecast was created  """  
      self.AutoTransfer:bool = obj["AutoTransfer"]
      """  Auto Transfer flag  """  
      self.DemandReference:str = obj["DemandReference"]
      """  The reference from the incoming demand source.  Can be used to locate other forecast records that have been created by this demand.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The DemandContractHdr to which this Forecast is related.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this Forecast is related to.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  Will link the Forecast record to the DemandSchedule that created it.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Shipto.ShipToNum.  For future use.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date until this forecast is considered effective. for information purposes only. for future use.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The ParentPartNum field identifies the Parent Part for kit components.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  """  
      self.EDIUpdateDate:str = obj["EDIUpdateDate"]
      """  Last update done by EDI to the forecast  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ImportErrorMsg:str = obj["ImportErrorMsg"]
      """  Reason import of this record failed.  Blank implies no error occurred.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.DemandContractDemandContract:str = obj["DemandContractDemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
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
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ForecastRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this forecast  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.ForeQty:int = obj["ForeQty"]
      """  Forecast quantity  """  
      self.ForeQtyUOM:str = obj["ForeQtyUOM"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.PONum:str = obj["PONum"]
      """  Inbound Customer PO Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date the forecast was created  """  
      self.AutoTransfer:bool = obj["AutoTransfer"]
      """  Auto Transfer flag  """  
      self.DemandReference:str = obj["DemandReference"]
      """  The reference from the incoming demand source.  Can be used to locate other forecast records that have been created by this demand.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The DemandContractHdr to which this Forecast is related.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this Forecast is related to.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  Will link the Forecast record to the DemandSchedule that created it.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Shipto.ShipToNum.  For future use.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date until this forecast is considered effective. for information purposes only. for future use.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The ParentPartNum field identifies the Parent Part for kit components.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  """  
      self.EDIUpdateDate:str = obj["EDIUpdateDate"]
      """  Last update done by EDI to the forecast  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ImportErrorMsg:str = obj["ImportErrorMsg"]
      """  Reason import of this record failed.  Blank implies no error occurred.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DemandContractDemandContract:str = obj["DemandContractDemandContract"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ClearForecasts_input:
   """ Required : 
   plAllPlants
   pdFromDate
   """  
   def __init__(self, obj):
      self.plAllPlants:bool = obj["plAllPlants"]
      """  If TRUE, clear all plants; if FALSE, clear Current Plant.  """  
      self.pdFromDate:str = obj["pdFromDate"]
      """  Only Forecast records on or after the given date will be deleted.  """  
      pass

class ClearForecasts_output:
   def __init__(self, obj):
      pass

class ClearShipToForecasts_output:
   def __init__(self, obj):
      pass

class ConvertForecastsToCSV_input:
   """ Required : 
   ds
   exportFilename
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      self.exportFilename:str = obj["exportFilename"]
      """  Name of the new file to be converted  """  
      pass

class ConvertForecastsToCSV_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  File Path on server  """  
      pass

   def parameters(self, obj):
      self.count:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   partNum
   plant
   custNum
   foreDate
   attributeSetID
   parentPartNum
   shipToNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.custNum:int = obj["custNum"]
      self.foreDate:str = obj["foreDate"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.parentPartNum:str = obj["parentPartNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ForecastAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.CustNum:int = obj["CustNum"]
      self.ForeDate:str = obj["ForeDate"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      self.ShipToNum:str = obj["ShipToNum"]
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

class Erp_Tablesets_ForecastImportExportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this plant assigned by the user.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  A blank CustID is used for a non-Customer-specific forecast.  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.ForeQty:int = obj["ForeQty"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.ImportErrorMsg:str = obj["ImportErrorMsg"]
      """  Reason import of this record failed.  Blank implies no error occurred.  """  
      self.ExtFcstPeriod:str = obj["ExtFcstPeriod"]
      """  External forecast period  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ForecastImportExportTableset:
   def __init__(self, obj):
      self.ForecastImportExport:list[Erp_Tablesets_ForecastImportExportRow] = obj["ForecastImportExport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ForecastListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this forecast  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.ForeQty:int = obj["ForeQty"]
      """  Forecast quantity  """  
      self.ForeQtyUOM:str = obj["ForeQtyUOM"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.PONum:str = obj["PONum"]
      """  Inbound Customer PO Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date the forecast was created  """  
      self.AutoTransfer:bool = obj["AutoTransfer"]
      """  Auto Transfer flag  """  
      self.DemandReference:str = obj["DemandReference"]
      """  The reference from the incoming demand source.  Can be used to locate other forecast records that have been created by this demand.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The DemandContractHdr to which this Forecast is related.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this Forecast is related to.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  Will link the Forecast record to the DemandSchedule that created it.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Shipto.ShipToNum.  For future use.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date until this forecast is considered effective. for information purposes only. for future use.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The ParentPartNum field identifies the Parent Part for kit components.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  """  
      self.EDIUpdateDate:str = obj["EDIUpdateDate"]
      """  Last update done by EDI to the forecast  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ImportErrorMsg:str = obj["ImportErrorMsg"]
      """  Reason import of this record failed.  Blank implies no error occurred.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.DemandContractDemandContract:str = obj["DemandContractDemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
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
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ForecastListTableset:
   def __init__(self, obj):
      self.ForecastList:list[Erp_Tablesets_ForecastListRow] = obj["ForecastList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ForecastRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.Plant:str = obj["Plant"]
      """  Site id for this forecast  """  
      self.ForeDate:str = obj["ForeDate"]
      """  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.ForeQty:int = obj["ForeQty"]
      """  Forecast quantity  """  
      self.ForeQtyUOM:str = obj["ForeQtyUOM"]
      self.ConsumedQty:int = obj["ConsumedQty"]
      """  The current accumulated quantity from all the order releases that fall within the forecast horizon.  """  
      self.PONum:str = obj["PONum"]
      """  Inbound Customer PO Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date the forecast was created  """  
      self.AutoTransfer:bool = obj["AutoTransfer"]
      """  Auto Transfer flag  """  
      self.DemandReference:str = obj["DemandReference"]
      """  The reference from the incoming demand source.  Can be used to locate other forecast records that have been created by this demand.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The DemandContractHdr to which this Forecast is related.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this Forecast is related to.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  Will link the Forecast record to the DemandSchedule that created it.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Shipto.ShipToNum.  For future use.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date until this forecast is considered effective. for information purposes only. for future use.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  The ParentPartNum field identifies the Parent Part for kit components.  """  
      self.KitFlag:str = obj["KitFlag"]
      """   A character flag field used to differentiate between kit component types
P = Kit Parent line
C = Kit Component Line
Null = regular line  """  
      self.EDIUpdateDate:str = obj["EDIUpdateDate"]
      """  Last update done by EDI to the forecast  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ImportErrorMsg:str = obj["ImportErrorMsg"]
      """  Reason import of this record failed.  Blank implies no error occurred.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.DemandContractDemandContract:str = obj["DemandContractDemandContract"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ForecastSalesHistoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.SellingShipQty:str = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed (or MISSING)  """  
      self.CustID:str = obj["CustID"]
      """  Customer associated with invoice  """  
      self.Plant:str = obj["Plant"]
      """  Plant associated with invoice.  """  
      self.StartYear:int = obj["StartYear"]
      """  Year of the first period for this sales history export.  """  
      self.StartPeriod:int = obj["StartPeriod"]
      """  Period of the year corresponding to the first available sales history.  """  
      self.PeriodsPerYear:int = obj["PeriodsPerYear"]
      """  Periods per year  """  
      self.PeriodsPerCycle:int = obj["PeriodsPerCycle"]
      """  Periods per cycle.  """  
      self.PeriodDate:str = obj["PeriodDate"]
      """  Date of this period  """  
      self.PeriodName:str = obj["PeriodName"]
      """  Name of this period  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part Description  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ForecastSalesHistoryTableset:
   def __init__(self, obj):
      self.ForecastSalesHistory:list[Erp_Tablesets_ForecastSalesHistoryRow] = obj["ForecastSalesHistory"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ForecastTableset:
   def __init__(self, obj):
      self.Forecast:list[Erp_Tablesets_ForecastRow] = obj["Forecast"]
      self.ForecastAttch:list[Erp_Tablesets_ForecastAttchRow] = obj["ForecastAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtForecastTableset:
   def __init__(self, obj):
      self.Forecast:list[Erp_Tablesets_ForecastRow] = obj["Forecast"]
      self.ForecastAttch:list[Erp_Tablesets_ForecastAttchRow] = obj["ForecastAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportForecasts_input:
   """ Required : 
   ds
   whereClauseForecast
   pdFromDate
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      self.whereClauseForecast:str = obj["whereClauseForecast"]
      """  (optional)Additional Where conditions for Forecast table.  """  
      self.pdFromDate:str = obj["pdFromDate"]
      """  (optional)Only records on or after the given date will be considered for import.  """  
      self.pageSize:int = obj["pageSize"]
      """  For future use.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  For future use.  """  
      pass

class ExportForecasts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   partNum
   plant
   custNum
   foreDate
   attributeSetID
   parentPartNum
   shipToNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.custNum:int = obj["custNum"]
      self.foreDate:str = obj["foreDate"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.parentPartNum:str = obj["parentPartNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ForecastTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ForecastTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ForecastTableset] = obj["returnObj"]
      pass

class GetForecastDays_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipPlant
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      """  Attribute Set ID  """  
      self.ipPlant:str = obj["ipPlant"]
      """  Site  """  
      pass

class GetForecastDays_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.piDaysBefore:int = obj["parameters"]
      self.piDaysAfter:int = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_ForecastListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewForecastAttch_input:
   """ Required : 
   ds
   partNum
   plant
   custNum
   foreDate
   attributeSetID
   parentPartNum
   shipToNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.custNum:int = obj["custNum"]
      self.foreDate:str = obj["foreDate"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.parentPartNum:str = obj["parentPartNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetNewForecastAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewForecastImportExport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      pass

class GetNewForecastImportExport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewForecast_input:
   """ Required : 
   ds
   partNum
   plant
   custNum
   foreDate
   attributeSetID
   parentPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.plant:str = obj["plant"]
      self.custNum:int = obj["custNum"]
      self.foreDate:str = obj["foreDate"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.parentPartNum:str = obj["parentPartNum"]
      pass

class GetNewForecast_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNextDateNewForecast_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastTableset] = obj["ds"]
      pass

class GetNextDateNewForecast_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  DateTime used for the next Forecast to be added  """  
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseForecast
   whereClauseForecastAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseForecast:str = obj["whereClauseForecast"]
      self.whereClauseForecastAttch:str = obj["whereClauseForecastAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ForecastTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSalesHistory_input:
   """ Required : 
   pdBeginDate
   pdEndDate
   pcCustList
   pcCustGrpList
   pcPartList
   pcProdGrpList
   pcPlantList
   pcOutputFile
   pcOutputFormat
   """  
   def __init__(self, obj):
      self.pdBeginDate:str = obj["pdBeginDate"]
      """  Begin Date of Sales to extract.  """  
      self.pdEndDate:str = obj["pdEndDate"]
      """  End Date of Sales to extract.  """  
      self.pcCustList:str = obj["pcCustList"]
      """  Tilde-delimited list of Customer Numbers for Sales extract.  Blank means all.  """  
      self.pcCustGrpList:str = obj["pcCustGrpList"]
      """  Tilde-delimited list of Customer Group Codes for Sales extract.  Blank means all.  """  
      self.pcPartList:str = obj["pcPartList"]
      """  Tilde-delimited list of Part Numbers for Sales extract.  Blank means all.  """  
      self.pcProdGrpList:str = obj["pcProdGrpList"]
      """  Tilde-delimited list of Product Group Codes for Sales extract.  Blank means all.  """  
      self.pcPlantList:str = obj["pcPlantList"]
      """  Tilde-delimited list of Plants for Sales extract.  Blank means all.  """  
      self.pcOutputFile:str = obj["pcOutputFile"]
      """  Export file path.  """  
      self.pcOutputFormat:str = obj["pcOutputFormat"]
      """  Export output format.  """  
      pass

class GetSalesHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ForecastSalesHistoryTableset] = obj["returnObj"]
      pass

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

class ImportExternalForecast_input:
   """ Required : 
   pcImportFormat
   pcImportFile
   """  
   def __init__(self, obj):
      self.pcImportFormat:str = obj["pcImportFormat"]
      """  Import file format.  """  
      self.pcImportFile:str = obj["pcImportFile"]
      """  Import file path.  """  
      pass

class ImportExternalForecast_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ForecastImportExportTableset] = obj["returnObj"]
      pass

class ImportForecastsReadFile_input:
   """ Required : 
   ds
   fileName
   importFormat
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      self.fileName:str = obj["fileName"]
      """  Path to the file to import  """  
      self.importFormat:str = obj["importFormat"]
      """  Import format  """  
      pass

class ImportForecastsReadFile_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  Number of rows imported  """  
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ImportForecasts_input:
   """ Required : 
   ds
   pcImportOptions
   plAllPlants
   pdFromDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      self.pcImportOptions:str = obj["pcImportOptions"]
      """  Valid choices are "A"=Add+Replace, "C"=Clear+Reload, "N"=New.  """  
      self.plAllPlants:bool = obj["plAllPlants"]
      """  If TRUE, clear all plants; if FALSE, clear Current Plant.  """  
      self.pdFromDate:str = obj["pdFromDate"]
      """  Only records on or after the given date will be considered for import.  """  
      pass

class ImportForecasts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastImportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class IsConfigurable_input:
   """ Required : 
   pcPartNum
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      pass

class IsConfigurable_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangingShipTo_input:
   """ Required : 
   shipTo
   custNum
   """  
   def __init__(self, obj):
      self.shipTo:str = obj["shipTo"]
      self.custNum:int = obj["custNum"]
      pass

class OnChangingShipTo_output:
   def __init__(self, obj):
      pass

class PartsAttributeClassHasRevisionAndIsMRPTracked_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      """  current Attribute Class ID  """  
      pass

class PartsAttributeClassHasRevisionAndIsMRPTracked_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateAttributeSetIDFromRevisionNum_input:
   """ Required : 
   partNum
   revisionNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  current part number  """  
      self.revisionNum:str = obj["revisionNum"]
      """  new revision selected  """  
      pass

class UpdateAttributeSetIDFromRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetID:int = obj["parameters"]
      self.planningAttributeSetSeq:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtForecastTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtForecastTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ForecastTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ForecastTableset] = obj["ds"]
      pass

      """  output parameters  """  

