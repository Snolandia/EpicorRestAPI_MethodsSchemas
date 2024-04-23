import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TariffSvc
# Description: Tariff table Maintenance.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Tariffs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Tariffs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Tariffs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TariffRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/Tariffs",headers=creds) as resp:
           return await resp.json()

async def post_Tariffs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Tariffs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TariffRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TariffRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/Tariffs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Tariffs_Company_TariffCode(Company, TariffCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Tariff item
   Description: Calls GetByID to retrieve the Tariff item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Tariff
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TariffCode: Desc: TariffCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TariffRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/Tariffs(" + Company + "," + TariffCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Tariffs_Company_TariffCode(Company, TariffCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Tariff for the service
   Description: Calls UpdateExt to update Tariff. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Tariff
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TariffCode: Desc: TariffCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TariffRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/Tariffs(" + Company + "," + TariffCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Tariffs_Company_TariffCode(Company, TariffCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Tariff item
   Description: Call UpdateExt to delete Tariff item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Tariff
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TariffCode: Desc: TariffCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/Tariffs(" + Company + "," + TariffCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Tariffs_Company_TariffCode_TariffComms(Company, TariffCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TariffComms items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TariffComms1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TariffCode: Desc: TariffCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TariffCommRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/Tariffs(" + Company + "," + TariffCode + ")/TariffComms",headers=creds) as resp:
           return await resp.json()

async def get_Tariffs_Company_TariffCode_TariffComms_Company_TariffCode_CommodityCode(Company, TariffCode, CommodityCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TariffComm item
   Description: Calls GetByID to retrieve the TariffComm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TariffComm1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TariffCode: Desc: TariffCode   Required: True   Allow empty value : True
      :param CommodityCode: Desc: CommodityCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TariffCommRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/Tariffs(" + Company + "," + TariffCode + ")/TariffComms(" + Company + "," + TariffCode + "," + CommodityCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_TariffComms(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TariffComms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TariffComms
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TariffCommRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/TariffComms",headers=creds) as resp:
           return await resp.json()

async def post_TariffComms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TariffComms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TariffCommRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TariffCommRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/TariffComms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TariffComms_Company_TariffCode_CommodityCode(Company, TariffCode, CommodityCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TariffComm item
   Description: Calls GetByID to retrieve the TariffComm item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TariffComm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TariffCode: Desc: TariffCode   Required: True   Allow empty value : True
      :param CommodityCode: Desc: CommodityCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TariffCommRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/TariffComms(" + Company + "," + TariffCode + "," + CommodityCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TariffComms_Company_TariffCode_CommodityCode(Company, TariffCode, CommodityCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TariffComm for the service
   Description: Calls UpdateExt to update TariffComm. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TariffComm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TariffCode: Desc: TariffCode   Required: True   Allow empty value : True
      :param CommodityCode: Desc: CommodityCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TariffCommRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/TariffComms(" + Company + "," + TariffCode + "," + CommodityCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TariffComms_Company_TariffCode_CommodityCode(Company, TariffCode, CommodityCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TariffComm item
   Description: Call UpdateExt to delete TariffComm item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TariffComm
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TariffCode: Desc: TariffCode   Required: True   Allow empty value : True
      :param CommodityCode: Desc: CommodityCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/TariffComms(" + Company + "," + TariffCode + "," + CommodityCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TariffListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTariff, whereClauseTariffComm, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTariff=" + whereClauseTariff
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTariffComm=" + whereClauseTariffComm
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tariffCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "tariffCode=" + tariffCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnCommCodeChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnCommCodeChange
   Description: Validates the Commodity Code.
   OperationID: OnCommCodeChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnCommCodeChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCommCodeChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTariff(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTariff
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTariff
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTariff_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTariff_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTariffComm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTariffComm
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTariffComm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTariffComm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTariffComm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TariffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TariffCommRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TariffCommRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TariffListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TariffListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TariffRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TariffRow] = obj["value"]
      pass

class Erp_Tablesets_TariffCommRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  The unique Tariff Code within the Company.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.GlobalTariffComm:bool = obj["GlobalTariffComm"]
      """  Marks this TariffComm as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TariffListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  The unique Tariff Code within the Company.  """  
      self.Description:str = obj["Description"]
      """  Unique Tariff description.  """  
      self.PrefSchemeID:str = obj["PrefSchemeID"]
      """  A unique Preference Scheme ID within the Company.  """  
      self.TariffRate:int = obj["TariffRate"]
      """  Tariff Rate that will be used to calculate the Duty Amount portion of the Landed Cost.  This is the rate applied to the total quantity of the container shipment line.  Tariff Rate is not applied on Tariff Percent or Specific Duty Amount.  """  
      self.TariffPercent:int = obj["TariffPercent"]
      """  Tariff Percent will be used to calculate the Duty Amount portion of the Landed Cost.  This is the percent rate applied to the total value of the container shipment line.  Tariff Percent is not applied on Tariff Rate or Specific Duty Amount.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  Amount added to the total value of the shipment line after applying the rate and percent.  """  
      self.MinDutyAmt:int = obj["MinDutyAmt"]
      """  If total calculated duty amount ((total shipment qty * Tariff Rate) + (total shipment value * Tariff Percent) + Specific Duty Amount) is less than the Minimum Duty Amount then the Minimum Duty Amount is used.  """  
      self.MaxDutyAmt:int = obj["MaxDutyAmt"]
      """  If total calculated duty amount ((total shipment qty * Tariff Rate) + (total shipment value * Tariff Percent) + Specific Duty Amount) is more than the Maximum Duty Amount then the Maximum Duty Amount is used.  """  
      self.GlobalTariff:bool = obj["GlobalTariff"]
      """  Marks this Tariff as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrefSchemeIDDescription:str = obj["PrefSchemeIDDescription"]
      """  Unique Preference Scheme description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TariffRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  The unique Tariff Code within the Company.  """  
      self.Description:str = obj["Description"]
      """  Unique Tariff description.  """  
      self.PrefSchemeID:str = obj["PrefSchemeID"]
      """  A unique Preference Scheme ID within the Company.  """  
      self.TariffRate:int = obj["TariffRate"]
      """  Tariff Rate that will be used to calculate the Duty Amount portion of the Landed Cost.  This is the rate applied to the total quantity of the container shipment line.  Tariff Rate is not applied on Tariff Percent or Specific Duty Amount.  """  
      self.TariffPercent:int = obj["TariffPercent"]
      """  Tariff Percent will be used to calculate the Duty Amount portion of the Landed Cost.  This is the percent rate applied to the total value of the container shipment line.  Tariff Percent is not applied on Tariff Rate or Specific Duty Amount.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  Amount added to the total value of the shipment line after applying the rate and percent.  """  
      self.MinDutyAmt:int = obj["MinDutyAmt"]
      """  If total calculated duty amount ((total shipment qty * Tariff Rate) + (total shipment value * Tariff Percent) + Specific Duty Amount) is less than the Minimum Duty Amount then the Minimum Duty Amount is used.  """  
      self.MaxDutyAmt:int = obj["MaxDutyAmt"]
      """  If total calculated duty amount ((total shipment qty * Tariff Rate) + (total shipment value * Tariff Percent) + Specific Duty Amount) is more than the Maximum Duty Amount then the Maximum Duty Amount is used.  """  
      self.GlobalTariff:bool = obj["GlobalTariff"]
      """  Marks this Tariff as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PrefSchemeIDDescription:str = obj["PrefSchemeIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tariffCode
   """  
   def __init__(self, obj):
      self.tariffCode:str = obj["tariffCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TariffCommRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  The unique Tariff Code within the Company.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.GlobalTariffComm:bool = obj["GlobalTariffComm"]
      """  Marks this TariffComm as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TariffListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  The unique Tariff Code within the Company.  """  
      self.Description:str = obj["Description"]
      """  Unique Tariff description.  """  
      self.PrefSchemeID:str = obj["PrefSchemeID"]
      """  A unique Preference Scheme ID within the Company.  """  
      self.TariffRate:int = obj["TariffRate"]
      """  Tariff Rate that will be used to calculate the Duty Amount portion of the Landed Cost.  This is the rate applied to the total quantity of the container shipment line.  Tariff Rate is not applied on Tariff Percent or Specific Duty Amount.  """  
      self.TariffPercent:int = obj["TariffPercent"]
      """  Tariff Percent will be used to calculate the Duty Amount portion of the Landed Cost.  This is the percent rate applied to the total value of the container shipment line.  Tariff Percent is not applied on Tariff Rate or Specific Duty Amount.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  Amount added to the total value of the shipment line after applying the rate and percent.  """  
      self.MinDutyAmt:int = obj["MinDutyAmt"]
      """  If total calculated duty amount ((total shipment qty * Tariff Rate) + (total shipment value * Tariff Percent) + Specific Duty Amount) is less than the Minimum Duty Amount then the Minimum Duty Amount is used.  """  
      self.MaxDutyAmt:int = obj["MaxDutyAmt"]
      """  If total calculated duty amount ((total shipment qty * Tariff Rate) + (total shipment value * Tariff Percent) + Specific Duty Amount) is more than the Maximum Duty Amount then the Maximum Duty Amount is used.  """  
      self.GlobalTariff:bool = obj["GlobalTariff"]
      """  Marks this Tariff as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrefSchemeIDDescription:str = obj["PrefSchemeIDDescription"]
      """  Unique Preference Scheme description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TariffListTableset:
   def __init__(self, obj):
      self.TariffList:list[Erp_Tablesets_TariffListRow] = obj["TariffList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TariffRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TariffCode:str = obj["TariffCode"]
      """  The unique Tariff Code within the Company.  """  
      self.Description:str = obj["Description"]
      """  Unique Tariff description.  """  
      self.PrefSchemeID:str = obj["PrefSchemeID"]
      """  A unique Preference Scheme ID within the Company.  """  
      self.TariffRate:int = obj["TariffRate"]
      """  Tariff Rate that will be used to calculate the Duty Amount portion of the Landed Cost.  This is the rate applied to the total quantity of the container shipment line.  Tariff Rate is not applied on Tariff Percent or Specific Duty Amount.  """  
      self.TariffPercent:int = obj["TariffPercent"]
      """  Tariff Percent will be used to calculate the Duty Amount portion of the Landed Cost.  This is the percent rate applied to the total value of the container shipment line.  Tariff Percent is not applied on Tariff Rate or Specific Duty Amount.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  Amount added to the total value of the shipment line after applying the rate and percent.  """  
      self.MinDutyAmt:int = obj["MinDutyAmt"]
      """  If total calculated duty amount ((total shipment qty * Tariff Rate) + (total shipment value * Tariff Percent) + Specific Duty Amount) is less than the Minimum Duty Amount then the Minimum Duty Amount is used.  """  
      self.MaxDutyAmt:int = obj["MaxDutyAmt"]
      """  If total calculated duty amount ((total shipment qty * Tariff Rate) + (total shipment value * Tariff Percent) + Specific Duty Amount) is more than the Maximum Duty Amount then the Maximum Duty Amount is used.  """  
      self.GlobalTariff:bool = obj["GlobalTariff"]
      """  Marks this Tariff as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PrefSchemeIDDescription:str = obj["PrefSchemeIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TariffTableset:
   def __init__(self, obj):
      self.Tariff:list[Erp_Tablesets_TariffRow] = obj["Tariff"]
      self.TariffComm:list[Erp_Tablesets_TariffCommRow] = obj["TariffComm"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTariffTableset:
   def __init__(self, obj):
      self.Tariff:list[Erp_Tablesets_TariffRow] = obj["Tariff"]
      self.TariffComm:list[Erp_Tablesets_TariffCommRow] = obj["TariffComm"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   tariffCode
   """  
   def __init__(self, obj):
      self.tariffCode:str = obj["tariffCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TariffTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TariffTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TariffTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TariffListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTariffComm_input:
   """ Required : 
   ds
   tariffCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TariffTableset] = obj["ds"]
      self.tariffCode:str = obj["tariffCode"]
      pass

class GetNewTariffComm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TariffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTariff_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TariffTableset] = obj["ds"]
      pass

class GetNewTariff_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TariffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTariff
   whereClauseTariffComm
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTariff:str = obj["whereClauseTariff"]
      self.whereClauseTariffComm:str = obj["whereClauseTariffComm"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TariffTableset] = obj["returnObj"]
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

class OnCommCodeChange_input:
   """ Required : 
   ipCommCodeID
   ds
   """  
   def __init__(self, obj):
      self.ipCommCodeID:str = obj["ipCommCodeID"]
      """  The Commodity Code ID  """  
      self.ds:list[Erp_Tablesets_TariffTableset] = obj["ds"]
      pass

class OnCommCodeChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TariffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTariffTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTariffTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TariffTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TariffTableset] = obj["ds"]
      pass

      """  output parameters  """  

