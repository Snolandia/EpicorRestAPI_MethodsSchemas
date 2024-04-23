import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TransOrderShipSvc
# Description: TransOrderShipSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TransOrderShips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransOrderShips
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips",headers=creds) as resp:
           return await resp.json()

async def post_TransOrderShips(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TransOrderShips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum(Company, PackNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TransOrderShip item
   Description: Calls GetByID to retrieve the TransOrderShip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransOrderShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TransOrderShips_Company_PackNum(Company, PackNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TransOrderShip for the service
   Description: Calls UpdateExt to update TransOrderShip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransOrderShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TransOrderShips_Company_PackNum(Company, PackNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TransOrderShip item
   Description: Call UpdateExt to delete TransOrderShip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransOrderShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipDtls(Company, PackNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TFShipDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipDtls",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipDtl item
   Description: Calls GetByID to retrieve the TFShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_CartonTrkDtls(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CartonTrkDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CartonTrkDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/CartonTrkDtls",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, PackNum, ShipmentType, CaseNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param CaseNum: Desc: CaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipHeadInsurances(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TFShipHeadInsurances items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipHeadInsurances1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadInsurances",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipHeadInsurances_Company_PackNum_InsuranceSeq(Company, PackNum, InsuranceSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipHeadInsurance item
   Description: Calls GetByID to retrieve the TFShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadInsurance1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipHeadTrailers(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TFShipHeadTrailers items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipHeadTrailers1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadTrailers",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipHeadTrailers_Company_PackNum_LicensePlate(Company, PackNum, LicensePlate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipHeadTrailer item
   Description: Calls GetByID to retrieve the TFShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadTrailer1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipUPS(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TFShipUPS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipUPS1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipUPS",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipUP item
   Description: Calls GetByID to retrieve the TFShipUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipUP1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipHeadAttches(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TFShipHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderShips_Company_PackNum_TFShipHeadAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipHeadAttch item
   Description: Calls GetByID to retrieve the TFShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TransOrderShips(" + Company + "," + PackNum + ")/TFShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFShipDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TFShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls",headers=creds) as resp:
           return await resp.json()

async def post_TFShipDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipDtl item
   Description: Calls GetByID to retrieve the TFShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TFShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TFShipDtl for the service
   Description: Calls UpdateExt to update TFShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TFShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TFShipDtl item
   Description: Call UpdateExt to delete TFShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFShipDtls_Company_PackNum_PackLine_ShipCOOs(Company, PackNum, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipCOOs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipCOOs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs",headers=creds) as resp:
           return await resp.json()

async def get_TFShipDtls_Company_PackNum_PackLine_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, PackNum, PackLine, RelatedToFile, OrigCountry, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipCOOs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipCOOs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipCOOs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs",headers=creds) as resp:
           return await resp.json()

async def post_ShipCOOs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipCOOs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipCOO for the service
   Description: Calls UpdateExt to update ShipCOO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipCOO item
   Description: Call UpdateExt to delete ShipCOO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def get_CartonTrkDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CartonTrkDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CartonTrkDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls",headers=creds) as resp:
           return await resp.json()

async def post_CartonTrkDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CartonTrkDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CartonTrkDtl for the service
   Description: Calls UpdateExt to update CartonTrkDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CartonTrkDtl item
   Description: Call UpdateExt to delete CartonTrkDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFShipHeadInsurances(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TFShipHeadInsurances items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipHeadInsurances
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances",headers=creds) as resp:
           return await resp.json()

async def post_TFShipHeadInsurances(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipHeadInsurances
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFShipHeadInsurances_Company_PackNum_InsuranceSeq(Company, PackNum, InsuranceSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipHeadInsurance item
   Description: Calls GetByID to retrieve the TFShipHeadInsurance item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TFShipHeadInsurances_Company_PackNum_InsuranceSeq(Company, PackNum, InsuranceSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TFShipHeadInsurance for the service
   Description: Calls UpdateExt to update TFShipHeadInsurance. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadInsuranceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TFShipHeadInsurances_Company_PackNum_InsuranceSeq(Company, PackNum, InsuranceSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TFShipHeadInsurance item
   Description: Call UpdateExt to delete TFShipHeadInsurance item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipHeadInsurance
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param InsuranceSeq: Desc: InsuranceSeq   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadInsurances(" + Company + "," + PackNum + "," + InsuranceSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFShipHeadTrailers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TFShipHeadTrailers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipHeadTrailers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers",headers=creds) as resp:
           return await resp.json()

async def post_TFShipHeadTrailers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipHeadTrailers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFShipHeadTrailers_Company_PackNum_LicensePlate(Company, PackNum, LicensePlate, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipHeadTrailer item
   Description: Calls GetByID to retrieve the TFShipHeadTrailer item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TFShipHeadTrailers_Company_PackNum_LicensePlate(Company, PackNum, LicensePlate, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TFShipHeadTrailer for the service
   Description: Calls UpdateExt to update TFShipHeadTrailer. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadTrailerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TFShipHeadTrailers_Company_PackNum_LicensePlate(Company, PackNum, LicensePlate, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TFShipHeadTrailer item
   Description: Call UpdateExt to delete TFShipHeadTrailer item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipHeadTrailer
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param LicensePlate: Desc: LicensePlate   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadTrailers(" + Company + "," + PackNum + "," + LicensePlate + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFShipUPS(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TFShipUPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipUPS
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS",headers=creds) as resp:
           return await resp.json()

async def post_TFShipUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFShipUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipUP item
   Description: Calls GetByID to retrieve the TFShipUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TFShipUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TFShipUP for the service
   Description: Calls UpdateExt to update TFShipUP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipUPSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TFShipUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TFShipUP item
   Description: Call UpdateExt to delete TFShipUP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFShipHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TFShipHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_TFShipHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFShipHeadAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipHeadAttch item
   Description: Calls GetByID to retrieve the TFShipHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TFShipHeadAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TFShipHeadAttch for the service
   Description: Calls UpdateExt to update TFShipHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TFShipHeadAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TFShipHeadAttch item
   Description: Call UpdateExt to delete TFShipHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/TFShipHeadAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTFShipHead, whereClauseTFShipHeadAttch, whereClauseTFShipDtl, whereClauseShipCOO, whereClauseCartonTrkDtl, whereClauseTFShipHeadInsurance, whereClauseTFShipHeadTrailer, whereClauseTFShipUPS, whereClauseLegalNumGenOpts, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseTFShipHead=" + whereClauseTFShipHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFShipHeadAttch=" + whereClauseTFShipHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFShipDtl=" + whereClauseTFShipDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipCOO=" + whereClauseShipCOO
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCartonTrkDtl=" + whereClauseCartonTrkDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFShipHeadInsurance=" + whereClauseTFShipHeadInsurance
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFShipHeadTrailer=" + whereClauseTFShipHeadTrailer
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFShipUPS=" + whereClauseTFShipUPS
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(packNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "packNum=" + packNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ExpireDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExpireDate
   Description: ExpireDate
   OperationID: ExpireDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExpireDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExpireDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CallsCreateCustomerCartons(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CallsCreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipPackNum">Current packNum</param><param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:  Called from Kinetic so first need to dirty rows
   OperationID: CallsCreateCustomerCartons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CallsCreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CallsCreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateCustomerCartons(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:
   OperationID: CreateCustomerCartons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CartonValidateWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CartonValidateWeight
   Description: Purpose:
<param name="ipWeight"> weight to validate</param>
Notes:
   OperationID: CartonValidateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CartonValidateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CartonValidateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeletePhantomPacks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePhantomPacks
   Description: Purpose:
<param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeletePhantomPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRangePhantomPacks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRangePhantomPacks
   Description: Purpose:
<param name="ipFromCase">First case number to start deletes</param><param name="ipToCase">Last case number to delete</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeleteRangePhantomPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRangePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRangePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCartonPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCartonPackaging
   Description: Purpose: Obtain the carton pacakcing specs
<param name="ipPkgCode">package code</param><param name="opPkgHeight">package height</param><param name="opPkgWidth">package width</param><param name="opPkgLength">package length</param>
Notes:
   OperationID: GetCartonPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCartonPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCartonPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackWeightWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackWeightWithCarton
   Description: Purpose:Update the Pack Weight with the carton weight
<param name="ipPackNum">Pack Number to process</param><param name="ipOldWeight">Previous weight</param><param name="ipWeight">Current Case weight</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackWeightWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackWeightWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackWeightWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackCODWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackCODWithCarton
   Description: Purpose: Update pack COD amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero</param><param name="ipOldCOD">Previous COD</param><param name="ipCOD">Current Case COD</param><param name="ipFlag">Current COD flag value</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackCODWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackCODWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackCODWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackDeclaredWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackDeclaredWithCarton
   Description: Purpose:  Update Pack Delcared Value Amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero </param><param name="ipOldDeclared">Previous COD</param><param name="ipDeclared">Current Case COD</param><param name="ipDeclaredFlag">current setting of declared insurance</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackDeclaredWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackDeclaredWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackDeclaredWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckValidCartonWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckValidCartonWeight
   Description: Purpose: Ensure the carton weight is valid.
<param name="ipPackNum">Pack Num to validate weights</param>
Notes:
   OperationID: CheckValidCartonWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckValidCartonWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckValidCartonWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the subcontract shipment.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateWeight
   Description: calculate the weight of a carton based upon Part.Weight.
   OperationID: CalculateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePackOutLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePackOutLotNum
   Description: This methods validates PackOut.LotNum field
   OperationID: ChangePackOutLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackOutLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackOutLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStatus
   Description: This method will be called to perform a change in the header status.
   OperationID: ChangeStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFOrdDtlLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFOrdDtlLotNum
   Description: This methods creates PartLot record if criteria is met in CheckTFOrdDtlLotNum
This method should run when the TFOrdDtl.LotNum field changes AND
after the running of CheckTFOrdDtlLotNum (which potentially returns questions/errors).
   OperationID: ChangeTFOrdDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFOrdDtlOurStockQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFOrdDtlOurStockQty
   Description: This methods updates fields associated with TFOrdDtl.OurStockQty.
This method should run when the TFOrdDtl.DisplayShipQty field changes.
   OperationID: ChangeTFOrdDtlOurStockQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlOurStockQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlOurStockQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFOrdDtlOurStockQtyUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFOrdDtlOurStockQtyUOM
   Description: This methods updates fields associated with TFOrdDtl.OurStockQty.
This method should run when the TFOrdDtl.SellingQtyUOM field changes.
   OperationID: ChangeTFOrdDtlOurStockQtyUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlOurStockQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlOurStockQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFOrdDtlPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFOrdDtlPartNum
   Description: This method defaults fields associated with the partnum.
This method should run when the TFOrdDtl.PartNum field changes.
   OperationID: ChangeTFOrdDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFOrdDtlWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFOrdDtlWarehouseCode
   Description: This methods updates fields associated with TFOrdDtl.WarehouseCode.
This method should run when the TFOrdDtl.WarehouseCode field changes.
   OperationID: ChangeTFOrdDtlWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdDtlWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdDtlWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFShipDtlLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFShipDtlLotNum
   Description: This methods creates PartLot record if criteria is met in CheckTFShipDtlLotNum
This method should run when the TFShipDtl.LotNum field changes AND
after the running of CheckTFShipDtlLotNum (which potentially returns questions/errors).
   OperationID: ChangeTFShipDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFShipDtlOurStockShippedQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFShipDtlOurStockShippedQty
   Description: This methods updates fields associated with TFShipDtl.OurStockShippedQty.
This method should run when the TFShipDtl.DisplayShipQty field changes.
   OperationID: ChangeTFShipDtlOurStockShippedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlOurStockShippedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlOurStockShippedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFShipDtlPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFShipDtlPartNum
   Description: This method defaults fields associated with the partnum.
This method should run when the TFShipDtl.PartNum field changes.
   OperationID: ChangeTFShipDtlPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFShipDtlTFOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFShipDtlTFOrderLine
   Description: This methods updates TFShipDtl.ShippedQty if criteria is met in CheckTFShipDtlTFOrderLine
This method should run when the TFShipDtl.TFOrdLine field changes AND
after the running of CheckTFShipDtlTFOrderline (which potentially returns errors).
   OperationID: ChangeTFShipDtlTFOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlTFOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlTFOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFShipDtlTFOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFShipDtlTFOrderNum
   Description: This methods validates the TFShipDtl.TFOrdNum field and updates associated fields.
This method should run when the TFShipDtl.TFOrdNum field changes.
   OperationID: ChangeTFShipDtlTFOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlTFOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlTFOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFShipDtlWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFShipDtlWarehouseCode
   Description: This methods updates fields associated with TFShipDtl.WarehouseCode.
This method should run when the TFShipDtl.WarehouseCode field changes.
   OperationID: ChangeTFShipDtlWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipDtlWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipDtlWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTFShipDtlNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTFShipDtlNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingTFShipDtlNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTFShipDtlNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTFShipDtlNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTFShipDtlAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTFShipDtlAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingTFShipDtlAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTFShipDtlAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTFShipDtlAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTFOrdDtlNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTFOrdDtlNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingTFOrdDtlNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTFOrdDtlNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTFOrdDtlNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTFOrdDtlAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTFOrdDtlAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingTFOrdDtlAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTFOrdDtlAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTFOrdDtlAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TFShipDtl_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TFShipDtl_OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: TFShipDtl_OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TFShipDtl_OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TFShipDtl_OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TFOrdDtl_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TFOrdDtl_OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: TFOrdDtl_OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TFOrdDtl_OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TFOrdDtl_OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShipViaCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShipViaCode
   Description: Function to set default values related to ShipVia
   OperationID: OnChangeShipViaCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipViaCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipViaCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCOOPercents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCOOPercents
   Description: This method should be called before the user can exit the TF Order in the UI to ensure that
the Quantity and Value Percents defined for Country of Origin records equal 100.
   OperationID: CheckCOOPercents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOOPercents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOOPercents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDirectOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDirectOrderLine
   Description: This method is to be run before the CreateDirectOrderLine. Any message returned
needs to be displayed to the user.  If they answer no to any the messages
then don't run the CreateDirectOrderLine method.
   OperationID: CheckDirectOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDirectOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDirectOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOHQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOHQ
   Description: This method is to be run before the CreateDirectOrderLine check the on hand
quantity of the part.  It will return a message in inventoryMessage if the
on hand quantity is less than zero.  If inventory message isn't null, then
it needs to be displayed to the user.  If they answer no to the question
then don't run the CreateDirectOrderLine method.
   OperationID: CheckOHQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOHQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOHQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackOutBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackOutBinNum
   Description: This methods validates PackOut.BinNum field
   OperationID: CheckPackOutBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackOutLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackOutLotNum
   Description: This methods validates PackOut.LotNum field
   OperationID: CheckPackOutLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackOutOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackOutOrderLine
   Description: This methods validates PackOut.OrderLine field
   OperationID: CheckPackOutOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackOutPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackOutPartNum
   Description: This methods validates PackOut.PartNum field
   OperationID: CheckPackOutPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackOutTFOrdNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackOutTFOrdNum
   Description: This methods validates PackOut.TFOrdNum field
   OperationID: CheckPackOutTFOrdNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutTFOrdNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutTFOrdNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackOutWarehousecode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackOutWarehousecode
   Description: This methods validates PackOut.Warehousecode field
   OperationID: CheckPackOutWarehousecode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackOutWarehousecode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackOutWarehousecode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPrePartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrePartInfo
   Description: This method checks to see if there are any questions or issues with the part entered
and returns a message, a part number and if any substitutes exist.
   OperationID: CheckPrePartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrePartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrePartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTFOrdDtlLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTFOrdDtlLotNum
   Description: This method checks to see if there are any questions or issues with the lotnum entered
and returns a message, run this before ChangeTFOrdDtlLotNum
   OperationID: CheckTFOrdDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTFOrdDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTFOrdDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTFShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTFShipDtl
   Description: This method is to be run before update to ask the user any question that need to be
answered before the record(s) can be saved.  If the user answers no to any one of
the questions, then the update method should not be called.
   OperationID: CheckTFShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTFShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTFShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTFShipDtlLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTFShipDtlLotNum
   Description: This method checks to see if there are any questions or issues with the lotnum entered
and returns a message, run this before ChangeTFShipDtlLotNum
   OperationID: CheckTFShipDtlLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTFShipDtlLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTFShipDtlLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckTFShipDtlTFOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckTFShipDtlTFOrderLine
   Description: This method validates the TFShipDtl.TFOrdLine and returns potential errors.
Run this before running ChangeTFShipDtl.TFOrdLine.
   OperationID: CheckTFShipDtlTFOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckTFShipDtlTFOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTFShipDtlTFOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearConvertedManifest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearConvertedManifest
   Description: Purpose: Clear TFShipHead Manifest fields when Unfreighting.
<param name="ipPackNum">Pack Num to clear Manifest fields</param>
Notes:
   OperationID: ClearConvertedManifest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearConvertedManifest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearConvertedManifest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertToManifestUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertToManifestUOM
   Description: Purpose: Populate TFShipHead Manifest fields.
<param name="ipPackNum">Pack Num to populate Manifest fields</param>
Notes:
   OperationID: ConvertToManifestUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToManifestUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToManifestUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertUOM
   Description: This method converts a qty from one UOM to another
   OperationID: ConvertUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateDirectOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateDirectOrder
   Description: This method takes the the TranDirectOrder dataset and create the Transfer Order
Header records.  It will also create and send back a new TFShipHed record for the
UI to update.  The GetNewDirectOrder method must be called first.
   OperationID: CreateDirectOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDirectOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDirectOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateDirectOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateDirectOrderLine
   Description: This method takes the TranDirectOrder dataset and creates the Transfer Order
Detail record.  It will also create and send back a new TFShipDtl record for the
UI to update.  The GetNewDirectOrderLine method must be called first.
The update method to create the TFShipHed record must also be run before
GetNewDirectOrderLine is called.
   OperationID: CreateDirectOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateDirectOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateDirectOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMassShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMassShipDtl
   Description: This methods creates TFShipDtl records based on the quantities remaining to be
shipped from the transfer order.
   OperationID: CreateMassShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMassShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMassShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDirectOrderDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDirectOrderDS
   Description: This method takes the direct transfer order number tied to the packing slip
and returns the full Direct Order Dataset
   OperationID: GetDirectOrderDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDirectOrderDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectOrderDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDirectShipDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDirectShipDate
   Description: Sets the transfer ship date base on fromplant, toplant, and needbydate.
It's calculated using the needby date and subtracting the transfers days
held in the PltTranDef Table.  To be called when the TFOrdDtl.NeedByDate changes
   OperationID: GetDirectShipDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDirectShipDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDirectShipDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDirectOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDirectOrder
   Description: This method creates the default empty Transfer Order Header for the user to update
before calling the CreateShipmentDirectOrder (update Order, new Shipment)
   OperationID: GetNewDirectOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDirectOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDirectOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDirectOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDirectOrderLine
   Description: This method creates an empty Transfer Order Detail record for the user to update
before calling the CreateShipmentDirectOrderLine (update TFOrdDtl, new TFShipDtl)
This method replaces the GetNewShipDtl method for Direct Order Shipments
The TFOrdHed record is sent back as well for constraint reasons
   OperationID: GetNewDirectOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDirectOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDirectOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFromOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFromOrder
   Description: This methods creates a new packing slip with header information pulled from
the transfer order header.
   OperationID: GetNewFromOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFromOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFromOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFromOrderWithPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFromOrderWithPCID
   Description: This methods creates a new packing slip with header information pulled from
the transfer order header, preventing its execution when the transfer order have allocations with PCID.
   OperationID: GetNewFromOrderWithPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFromOrderWithPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFromOrderWithPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackaging
   Description: Purpose:
Parameters:
<param name="ipPkgCode">package code</param><param name="ds">Transfer Shipment data set</param>
Notes:
   OperationID: GetPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackClass
   Description: Purpose:
Parameters:
<param name="ipPkgClass">package class</param><param name="ds">Transfer Order Shipment data set</param>
Notes:
   OperationID: GetPackClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPayBTFlagDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPayBTFlagDefaults
   Description: Purpose:
Parameters:
<param name="ds">The transfer order data set</param>
Notes:
   OperationID: GetPayBTFlagDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPayBTFlagDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayBTFlagDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOPackaging
   Description: Purpose:
Parameters:
<param name="ipPkgCode">package code</param><param name="ds">Transfer PackOut data set</param>
Notes:
   OperationID: GetPOPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOPackClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOPackClass
   Description: Purpose:
Parameters:
<param name="ipPkgClass">package class</param><param name="ds">Packout data set</param>
Notes:
   OperationID: GetPOPackClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOPackClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOPackClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePOPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePOPartNum
   Description: Call this method when changing the packout part to maintain inventory tracking
   OperationID: ChangePOPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePOPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePOPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePORevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePORevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: ChangePORevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePORevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePORevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetScale(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetScale
   Description: Calls GetDefaultScale
   OperationID: GetScale
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetScale_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScale_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: GetTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetShipCOOTotals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetShipCOOTotals
   Description: Calculate Company of Origins totals in current tableset for certain Transfer Order Line.
The method is used in clients which don't have possibility to calculate it (in example Kinetic form)
   OperationID: GetShipCOOTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetShipCOOTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetShipCOOTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POChangeStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POChangeStatus
   Description: This method will be called to perform a change in the header status for the Pack Out screen.
   OperationID: POChangeStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POChangeStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POChangeStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POCreateDtlList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POCreateDtlList
   Description: This method copies the available Order Release lines to the PackOut datatable
for update
   OperationID: POCreateDtlList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POCreateDtlList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POCreateDtlList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POFindBuffer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POFindBuffer
   Description: This method returns a count order of lines that match the incomming scanned criteria.
If there is only 1 match, it will copy the order dtl data into the returning record.
If there is no unique match, logical fields are updated to que the UI as to what need
to be prompted in order to find a matching order dtl.
   OperationID: POFindBuffer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POFindBuffer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POFindBuffer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POGetDtlList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetDtlList
   Description: This method copies the available Carton Dtl lines to the PackOut datatable
for update
   OperationID: POGetDtlList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetDtlList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetDtlList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POGetNewWithDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetNewWithDtl
   Description: Return a tableset populated with PackOut header and detail list.
   OperationID: POGetNewWithDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetNewWithDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetNewWithDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDisablePackOut(epicorHeaders = None):
   """  
   Summary: Invoke method GetDisablePackOut
   Description: Get value of DisablePackOut from Plant Configuration.
   OperationID: GetDisablePackOut
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisablePackOut_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_POGetNew(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetNew
   Description: This method creates a new packout record for the customer shipment packout
screen
   OperationID: POGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POUndo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POUndo
   Description: This methods simulates Undo.
   OperationID: POUndo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUndo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUndo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POUpdate
   Description: This method creates a new packout record to create TFShiphed and TFShipDtl records
   OperationID: POUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_POUpdateHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POUpdateHeader
   Description: This methods simulates Undo.
   OperationID: POUpdateHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POUpdateHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POUpdateHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreDeleteDirectShip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreDeleteDirectShip
   Description: This method needs to be called before deleting line items.  It asks the
user if they want to delete the TFOrdDtl as well as the TFShipDtl.
   OperationID: PreDeleteDirectShip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreDeleteDirectShip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreDeleteDirectShip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreDeselectSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreDeselectSN
   Description: Sets PreDeselected before delete a TFOrdShipLine.
   OperationID: PreDeselectSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreDeselectSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreDeselectSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVEnable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVEnable
   Description: Purpose:
Parameters:
<param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ds">The transfer order data set</param>
Notes:
   OperationID: SetUPSQVEnable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVShipStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVShipStatus
   Description: Purpose:
Parameters:
<param name="ipShipStatus">Shipment status</param><param name="ds">The transfer shipment data set</param>
Notes:
   OperationID: SetUPSQVShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreShipPack(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreShipPack
   Description: Procedure to check in attribute sets are needed and valid.
If so, the transfer order shipment cannot be shipped
   OperationID: PreShipPack
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreShipPack_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreShipPack_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EADValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EADValidation
   Description: Validate Ship Date is not before the Earliest Apply Date.
   OperationID: EADValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EADValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EADValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ShipPackingSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ShipPackingSlip
   Description: This methods assigns the TFShipHead.Shipped field and updates/creates all of the
associated records (partbin, parttran, TFOrdHed, etc.) when a Packing Slip is shipped.
   OperationID: ShipPackingSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ShipPackingSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ShipPackingSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUnShipPack(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUnShipPack
   Description: Procedure to know if the order or at least one line was already received in the target plant.
If so, the transfer order shipment cannot be unshipped
   OperationID: PreUnShipPack
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUnShipPack_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUnShipPack_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnShipPackingSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnShipPackingSlip
   Description: This methods assigns the TFShipHead.Shipped field and updates/deletes all of the
associated records (parttran) when a Packing Slip is unshipped. Also potentially creates
partbin and partdtl records.
   OperationID: UnShipPackingSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnShipPackingSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnShipPackingSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBinCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBinCode
   Description: Purpose: Validate the bin.
<param name="ipWhse">Warehouse code used to edit bin</param><param name="ipBinNum">Bin Code to validate</param>
Notes:
   OperationID: ValidateBinCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBinCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBinCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePartNum
   Description: Purpose: This method is to be called when the Part Number field changes
<param name="ipPartNum">Part Number</param>
   OperationID: ValidatePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WarnNegativeBinOH(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WarnNegativeBinOH
   OperationID: WarnNegativeBinOH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNegativeBinOH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNegativeBinOH_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WarnNegativeBinQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WarnNegativeBinQty
   Description: Procedure used to warn if negative inventory in Bin.
   OperationID: WarnNegativeBinQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNegativeBinQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNegativeBinQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WarnNegativeLotOH(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WarnNegativeLotOH
   OperationID: WarnNegativeLotOH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarnNegativeLotOH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarnNegativeLotOH_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsSerialTracked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsSerialTracked
   Description: Purpose:  Returns true only if ipPart is serial tracked, and the Plant owning
ipWhse has full serial tracking enabled.
   OperationID: IsSerialTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsSerialTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsSerialTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GenerateDigitalSignature(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateDigitalSignature
   Description: Generate Digital Signature
   OperationID: GenerateDigitalSignature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDigitalSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDigitalSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEnablePackageControl(epicorHeaders = None):
   """  
   Summary: Invoke method GetEnablePackageControl
   OperationID: GetEnablePackageControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnablePackageControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCID
   OperationID: ChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFShipHeadTFOrdNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFShipHeadTFOrdNum
   OperationID: ChangeTFShipHeadTFOrdNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFShipHeadTFOrdNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFShipHeadTFOrdNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemovePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemovePCID
   Description: Back out pack detail lines related to a PCID
   OperationID: RemovePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemovePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemovePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFShipHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFShipHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFShipHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFShipHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipCOO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipCOO
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipCOO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipCOO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipCOO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCartonTrkDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCartonTrkDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCartonTrkDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCartonTrkDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCartonTrkDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFShipHeadInsurance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFShipHeadInsurance
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHeadInsurance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHeadInsurance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHeadInsurance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFShipHeadTrailer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFShipHeadTrailer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHeadTrailer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHeadTrailer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHeadTrailer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFShipUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFShipUPS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CartonTrkDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipCOORow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadInsuranceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipHeadInsuranceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadTrailerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipHeadTrailerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipUPSRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipUPSRow] = obj["value"]
      pass

class Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  """  
      self.PackNum:int = obj["PackNum"]
      """  The pack number associated with the tracking number.  """  
      self.CaseNum:int = obj["CaseNum"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.PkgWeight:int = obj["PkgWeight"]
      """  Package Weight  """  
      self.CODFlag:bool = obj["CODFlag"]
      """  Prefer COD delivery.  Reserved for future development.  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order.  Reserved for future development.  """  
      self.DeclaredValueFlag:bool = obj["DeclaredValueFlag"]
      """  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  """  
      self.DeclaredValue:int = obj["DeclaredValue"]
      """  Declared Insurance Amount.  Reserved for future development.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.CODValue:int = obj["CODValue"]
      """  Collect On Delivery Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CaseID:str = obj["CaseID"]
      """  Concatenated field consisting of PackNum and CaseNum separated by a dash.  """  
      self.PackStatus:str = obj["PackStatus"]
      """  Status of the shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  logical used by UI for row rules  """  
      self.CapturePt:str = obj["CapturePt"]
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.OrigCountry:int = obj["OrigCountry"]
      """  CountryNum for Country of Origin  """  
      self.QtyPerc:int = obj["QtyPerc"]
      """  Qty percent of this part which is from this country of origin.  """  
      self.ValuePerc:int = obj["ValuePerc"]
      """  Value percent of this part from this country of origin.  """  
      self.Primary:bool = obj["Primary"]
      """  Is this the primary country of origin for this part  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...).  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is defaulted as Job Number.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.requestdate:str = obj["requestdate"]
      """  requestdate  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Calculated price for the item being transferred.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Transfer Order.  This quantity is in the IUM unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AllocatedShippedQty:int = obj["AllocatedShippedQty"]
      """  If AMM is licensed this column will hold how much of this shipment was allocated prior to the shipment in case this shipment is ever "unshipped"  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      """  Are there available serial numbers?  """  
      self.direct_transfer:bool = obj["direct_transfer"]
      """  direct-transfer  """  
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockShippedQty * DimConvFactor  """  
      self.LineShipped:bool = obj["LineShipped"]
      """  Indicates if the Shipment line has been shipped  """  
      self.OrderShipmentQty:int = obj["OrderShipmentQty"]
      """  Current Shipment in OrderUOM  """  
      self.OrderUOM:str = obj["OrderUOM"]
      """  UOM from Transfer Order  """  
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by the freight web service  """  
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by the freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by the freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by the freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by the freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by the freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by the freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by the freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by the freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by the freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by the freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by the freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by the freight web service  """  
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by the freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by the freight web service  """  
      self.Received:bool = obj["Received"]
      """  Indicates if the Shipment line has been received  """  
      self.RemainingQty:int = obj["RemainingQty"]
      """  The remaining quantity  """  
      self.RequestQty:int = obj["RequestQty"]
      """  The request quantity  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  The shipped quantity  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Ship Status of the Transfer Order Shipment line, copied from the Transfer Order Shipment header.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      """  Enable Attribute Set Search  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
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

class Erp_Tablesets_TFShipHeadInsuranceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PackNum:int = obj["PackNum"]
      """  PackNum  """  
      self.InsuranceSeq:int = obj["InsuranceSeq"]
      """  InsuranceSeq  """  
      self.Type:str = obj["Type"]
      """  Insurance Type  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Insurance Company Name  """  
      self.PolicyNum:str = obj["PolicyNum"]
      """  Insurance Policy Number  """  
      self.Premium:int = obj["Premium"]
      """  Insurance Premium  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.directtransfer:bool = obj["directtransfer"]
      """  directtransfer  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Third address line  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFromAddr:str = obj["DspFromAddr"]
      """  Display for the Ship From Address  """  
      self.DspShipAddr:str = obj["DspShipAddr"]
      """  Display for the Ship To Address  """  
      self.TranStatus:str = obj["TranStatus"]
      """  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.TranStatusDescription:str = obj["TranStatusDescription"]
      """  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      """  Flag to control if the Shipped flag is enabled/disabled  """  
      self.SlipStatus:str = obj["SlipStatus"]
      """  Translated field of ShipStatus  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height prompt is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  1 = disable / 0 = enable  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for subcontract shipments  """  
      self.CalcPSPrices:bool = obj["CalcPSPrices"]
      """  Intended for internal use.  Indicates if prices are to be calculated  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if the transaction document type is available for input  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.PackClssDescription:str = obj["PackClssDescription"]
      """  Full description of the Packaging Classification.  """  
      self.PackingDescription:str = obj["PackingDescription"]
      """  Full description of Packing Code.  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.directtransfer:bool = obj["directtransfer"]
      """  directtransfer  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Third address line  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGCarrierCUIT:str = obj["AGCarrierCUIT"]
      """  AGCarrierCUIT  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.AGTrackLicense:str = obj["AGTrackLicense"]
      """  AGTrackLicense  """  
      self.AGShippingWay:str = obj["AGShippingWay"]
      """  AGShippingWay  """  
      self.AGCOTMark:bool = obj["AGCOTMark"]
      """  AGCOTMark  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Creation date and time  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Certificate Serial Number  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Certificate  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  Fiscal Folio (UUID)  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  SAT Certificate Serial Number  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Digital Seal  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  SAT Seal  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  Original String  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  TFD Original String  """  
      self.MXSerie:str = obj["MXSerie"]
      """  Serie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  Folio  """  
      self.MXETD:str = obj["MXETD"]
      """  Estimated Date and Time of Departure  """  
      self.MXETA:str = obj["MXETA"]
      """  Estimated Date and Time of Arrival  """  
      self.MXDistance:int = obj["MXDistance"]
      """  Distance in Km  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.MXCartaPorteStatus:str = obj["MXCartaPorteStatus"]
      """  Carta Porte Status  """  
      self.VehicleLicensePlate:str = obj["VehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.VehicleType:str = obj["VehicleType"]
      """  Vehicle Type  """  
      self.VehicleYear:int = obj["VehicleYear"]
      """  Vehicle Year  """  
      self.DriverID:str = obj["DriverID"]
      """  Driver  """  
      self.MXCancelFiscalFolio:str = obj["MXCancelFiscalFolio"]
      """  MXCancelFiscalFolio  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number.  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.DspFromAddr:str = obj["DspFromAddr"]
      """  Display for the Ship From Address  """  
      self.DspShipAddr:str = obj["DspShipAddr"]
      """  Display for the Ship To Address  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      """  Flag to control if the Shipped flag is enabled/disabled  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if the transaction document type is available for input  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for subcontract shipments  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height prompt is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  1 = disable / 0 = enable  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width is enabled.  """  
      self.SlipStatus:str = obj["SlipStatus"]
      """  Translated field of ShipStatus  """  
      self.TranStatus:str = obj["TranStatus"]
      """  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.TranStatusDescription:str = obj["TranStatusDescription"]
      """  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  """  
      self.VNAccordingToDemand:str = obj["VNAccordingToDemand"]
      self.VNCarrier:str = obj["VNCarrier"]
      self.VNContractNumber:str = obj["VNContractNumber"]
      self.VNDate:str = obj["VNDate"]
      self.VNFor:str = obj["VNFor"]
      self.VNFrom:str = obj["VNFrom"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.CalcPSPrices:bool = obj["CalcPSPrices"]
      """  Intended for internal use.  Indicates if prices are to be calculated  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Logical indicating if the package control functionality should be enabled.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer order number  """  
      self.MXETADate:str = obj["MXETADate"]
      """  Estimated Date of Arrival  """  
      self.MXETATime:int = obj["MXETATime"]
      """  Estimated Time of Arrival  """  
      self.MXETDDate:str = obj["MXETDDate"]
      """  Estimated Date of Departure  """  
      self.MXETDTime:int = obj["MXETDTime"]
      """  Estimated Time of Departure  """  
      self.EnablePhantom:bool = obj["EnablePhantom"]
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      self.MXVehicleWeight:int = obj["MXVehicleWeight"]
      """  Vehicle Weight (in tons)  """  
      self.MXIdCCP:str = obj["MXIdCCP"]
      """  A unique Carta Porte identification number assigned by Epicor  """  
      self.MXCustomsRegime:str = obj["MXCustomsRegime"]
      """  Customs Regime for Export transaction.  """  
      self.MXReverseLogistics:bool = obj["MXReverseLogistics"]
      """  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.AGLegalNumCnfgDescription:str = obj["AGLegalNumCnfgDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.PackClssDescription:str = obj["PackClssDescription"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadTrailerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip  """  
      self.LicensePlate:str = obj["LicensePlate"]
      """  License Plate for Trailer  """  
      self.Type:str = obj["Type"]
      """  Type of Trailer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipUPSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email Address  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Notify Email address when shipped  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating if the UPS Quantum View fields are to be enabled  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumber_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CalculateWeight_input:
   """ Required : 
   CartonNumber
   """  
   def __init__(self, obj):
      self.CartonNumber:int = obj["CartonNumber"]
      """  Carton Number  """  
      pass

class CalculateWeight_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.CalculatedWeight:int = obj["parameters"]
      pass

      """  output parameters  """  

class CallsCreateCustomerCartons_input:
   """ Required : 
   ipPackNum
   ipNbrCartonsToCreate
   ipPkgCode
   ipPkgLength
   ipPkgWidth
   ipPkgHeight
   ipRecalcAmts
   ipZeroWeight
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipNbrCartonsToCreate:int = obj["ipNbrCartonsToCreate"]
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ipPkgLength:int = obj["ipPkgLength"]
      self.ipPkgWidth:int = obj["ipPkgWidth"]
      self.ipPkgHeight:int = obj["ipPkgHeight"]
      self.ipRecalcAmts:bool = obj["ipRecalcAmts"]
      self.ipZeroWeight:bool = obj["ipZeroWeight"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class CallsCreateCustomerCartons_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CartonValidateWeight_input:
   """ Required : 
   ipWeight
   """  
   def __init__(self, obj):
      self.ipWeight:int = obj["ipWeight"]
      pass

class CartonValidateWeight_output:
   def __init__(self, obj):
      pass

class ChangePCID_input:
   """ Required : 
   ipPackNum
   ipPCID
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipPCID:str = obj["ipPCID"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.opAlreadyScannedPackNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class ChangePOPartNum_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The new part number  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class ChangePOPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePORevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class ChangePORevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePackOutLotNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class ChangePackOutLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeStatus_input:
   """ Required : 
   ipShipHedRowID
   ipStatus
   ds
   """  
   def __init__(self, obj):
      self.ipShipHedRowID:str = obj["ipShipHedRowID"]
      """  Unique Identifier for the Transfer Order Shipment  """  
      self.ipStatus:str = obj["ipStatus"]
      """  Selected Status.
           Valid Options: Open, Close, Void, UnVoid, Freight, UnFreight, Stage  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangeStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFOrdDtlLotNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class ChangeTFOrdDtlLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFOrdDtlOurStockQtyUOM_input:
   """ Required : 
   ipProposedSellingQtyUOM
   ds
   """  
   def __init__(self, obj):
      self.ipProposedSellingQtyUOM:str = obj["ipProposedSellingQtyUOM"]
      """  The new proposed TFOrdDtl.SellingQtyUOM value  """  
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class ChangeTFOrdDtlOurStockQtyUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFOrdDtlOurStockQty_input:
   """ Required : 
   ipProposedOurStockQty
   ds
   """  
   def __init__(self, obj):
      self.ipProposedOurStockQty:int = obj["ipProposedOurStockQty"]
      """  The new proposed TFOrdDtl.DisplayShipQty value  """  
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class ChangeTFOrdDtlOurStockQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFOrdDtlPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class ChangeTFOrdDtlPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFOrdDtlWarehouseCode_input:
   """ Required : 
   ipProposedWarehouseCode
   ds
   """  
   def __init__(self, obj):
      self.ipProposedWarehouseCode:str = obj["ipProposedWarehouseCode"]
      """  The new proposed TFOrdDtl.WarehouseCode value  """  
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class ChangeTFOrdDtlWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFShipDtlLotNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangeTFShipDtlLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFShipDtlOurStockShippedQty_input:
   """ Required : 
   packNum
   packLine
   ipProposedOurStockShippedQty
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Pack Number to be modified  """  
      self.packLine:int = obj["packLine"]
      """  Pack Line to be modified  """  
      self.ipProposedOurStockShippedQty:int = obj["ipProposedOurStockShippedQty"]
      """  The new proposed TFShipDtl.DisplayShipQty value  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangeTFShipDtlOurStockShippedQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      self.outNegQtyAction:str = obj["parameters"]
      self.outNetWeight:int = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeTFShipDtlPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangeTFShipDtlPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFShipDtlTFOrderLine_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangeTFShipDtlTFOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFShipDtlTFOrderNum_input:
   """ Required : 
   ipProposedTFOrdNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedTFOrdNum:str = obj["ipProposedTFOrdNum"]
      """  The new proposed TFShipDtl.TFOrdNum value  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangeTFShipDtlTFOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFShipDtlWarehouseCode_input:
   """ Required : 
   packNum
   packLine
   ipProposedWarehouseCode
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Pack Number to be modified  """  
      self.packLine:int = obj["packLine"]
      """  Pack Line to be modified  """  
      self.ipProposedWarehouseCode:str = obj["ipProposedWarehouseCode"]
      """  The new proposed TFShipDtl.WarehouseCode value  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangeTFShipDtlWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFShipHeadTFOrdNum_input:
   """ Required : 
   ipProposedTFOrdNum
   ds
   """  
   def __init__(self, obj):
      self.ipProposedTFOrdNum:str = obj["ipProposedTFOrdNum"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class ChangeTFShipHeadTFOrdNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCOOPercents_input:
   """ Required : 
   iPackNum
   iPackLine
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The pack number  """  
      self.iPackLine:int = obj["iPackLine"]
      """  The pack line number  """  
      pass

class CheckCOOPercents_output:
   def __init__(self, obj):
      pass

class CheckDirectOrderLine_input:
   """ Required : 
   tfShipHeadSysRowID
   ds
   """  
   def __init__(self, obj):
      self.tfShipHeadSysRowID:str = obj["tfShipHeadSysRowID"]
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class CheckDirectOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      self.allocationMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckOHQ_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class CheckOHQ_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      self.inventoryMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPackOutBinNum_input:
   """ Required : 
   ds
   ipBinNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.ipBinNum:str = obj["ipBinNum"]
      """  The new proposed BinNum value  """  
      pass

class CheckPackOutBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPackOutLotNum_input:
   """ Required : 
   ds
   ipLotNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.ipLotNum:str = obj["ipLotNum"]
      """  The new proposed LotNum value  """  
      pass

class CheckPackOutLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.vMsgText:str = obj["parameters"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPackOutOrderLine_input:
   """ Required : 
   ds
   ipOrderLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  The new proposed OrderLine value  """  
      pass

class CheckPackOutOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPackOutPartNum_input:
   """ Required : 
   ds
   ipPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.ipPartNum:str = obj["ipPartNum"]
      """  The new proposed PartNum value  """  
      pass

class CheckPackOutPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPackOutTFOrdNum_input:
   """ Required : 
   ds
   ipTFOrdNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.ipTFOrdNum:str = obj["ipTFOrdNum"]
      """  The new proposed TFOrdNum value  """  
      pass

class CheckPackOutTFOrdNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPackOutWarehousecode_input:
   """ Required : 
   ds
   ipWarehousecode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      self.ipWarehousecode:str = obj["ipWarehousecode"]
      """  The new proposed Warehousecode value  """  
      pass

class CheckPackOutWarehousecode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPrePartInfo_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The input-output part number to validate and it gets returned  """  
      pass

class CheckPrePartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.vMsgText:str = obj["parameters"]
      self.vSubAvail:bool = obj["vSubAvail"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckTFOrdDtlLotNum_input:
   """ Required : 
   ipLotNum
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipLotNum:str = obj["ipLotNum"]
      """  The lotnum to validate  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The value of the TFOrdDtl.PartNum used to locate partlot records  """  
      pass

class CheckTFOrdDtlLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMsgText:str = obj["parameters"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckTFShipDtlLotNum_input:
   """ Required : 
   ipLotNum
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipLotNum:str = obj["ipLotNum"]
      """  The lotnum to validate  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The value of the TFShipDtl.PartNum used to locate partlot records  """  
      pass

class CheckTFShipDtlLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMsgText:str = obj["parameters"]
      self.vMsgType:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckTFShipDtlTFOrderLine_input:
   """ Required : 
   ipPackNum
   ipPackLine
   ipProposedTFOrdLine
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  The packnum value of the TFShipDtl to check  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  The packline value of the TFShipDtl to check  """  
      self.ipProposedTFOrdLine:int = obj["ipProposedTFOrdLine"]
      """  The proposed TFOrdline value  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class CheckTFShipDtlTFOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckTFShipDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class CheckTFShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.allocationMessage:str = obj["parameters"]
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckValidCartonWeight_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class CheckValidCartonWeight_output:
   def __init__(self, obj):
      pass

class ClearConvertedManifest_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class ClearConvertedManifest_output:
   def __init__(self, obj):
      pass

class ConvertToManifestUOM_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class ConvertToManifestUOM_output:
   def __init__(self, obj):
      pass

class ConvertUOM_input:
   """ Required : 
   partNum
   baseQty
   baseUOM
   convUOM
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number  """  
      self.baseQty:int = obj["baseQty"]
      """  Qty you wish to convert  """  
      self.baseUOM:str = obj["baseUOM"]
      """  UOM baseQty is specified in  """  
      self.convUOM:str = obj["convUOM"]
      """  UOM to convert to  """  
      pass

class ConvertUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.convQty:int = obj["parameters"]
      pass

      """  output parameters  """  

class CreateCustomerCartons_input:
   """ Required : 
   ipNbrCartonsToCreate
   ipPkgCode
   ipPkgLength
   ipPkgWidth
   ipPkgHeight
   ipRecalcAmts
   ipZeroWeight
   ds
   """  
   def __init__(self, obj):
      self.ipNbrCartonsToCreate:int = obj["ipNbrCartonsToCreate"]
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ipPkgLength:int = obj["ipPkgLength"]
      self.ipPkgWidth:int = obj["ipPkgWidth"]
      self.ipPkgHeight:int = obj["ipPkgHeight"]
      self.ipRecalcAmts:bool = obj["ipRecalcAmts"]
      self.ipZeroWeight:bool = obj["ipZeroWeight"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class CreateCustomerCartons_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateDirectOrderLine_input:
   """ Required : 
   ipShipHeadRowID
   ds
   ds1
   """  
   def __init__(self, obj):
      self.ipShipHeadRowID:str = obj["ipShipHeadRowID"]
      """  Unique Identifier for the Transfer Order Shipment  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds1"]
      pass

class CreateDirectOrderLine_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class CreateDirectOrder_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class CreateDirectOrder_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateMassShipDtl_input:
   """ Required : 
   packNum
   orderNum
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Your existing packing slip number  """  
      self.orderNum:str = obj["orderNum"]
      """  The transfer order number  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class CreateMassShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeletePhantomPacks_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class DeletePhantomPacks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteRangePhantomPacks_input:
   """ Required : 
   ipFromCase
   ipToCase
   ds
   """  
   def __init__(self, obj):
      self.ipFromCase:int = obj["ipFromCase"]
      self.ipToCase:int = obj["ipToCase"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class DeleteRangePhantomPacks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class EADValidation_input:
   """ Required : 
   ShipDate
   """  
   def __init__(self, obj):
      self.ShipDate:str = obj["ShipDate"]
      """  Shipment Date  """  
      pass

class EADValidation_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  """  
      self.PackNum:int = obj["PackNum"]
      """  The pack number associated with the tracking number.  """  
      self.CaseNum:int = obj["CaseNum"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.PkgWeight:int = obj["PkgWeight"]
      """  Package Weight  """  
      self.CODFlag:bool = obj["CODFlag"]
      """  Prefer COD delivery.  Reserved for future development.  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order.  Reserved for future development.  """  
      self.DeclaredValueFlag:bool = obj["DeclaredValueFlag"]
      """  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  """  
      self.DeclaredValue:int = obj["DeclaredValue"]
      """  Declared Insurance Amount.  Reserved for future development.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.CODValue:int = obj["CODValue"]
      """  Collect On Delivery Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CaseID:str = obj["CaseID"]
      """  Concatenated field consisting of PackNum and CaseNum separated by a dash.  """  
      self.PackStatus:str = obj["PackStatus"]
      """  Status of the shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  logical used by UI for row rules  """  
      self.CapturePt:str = obj["CapturePt"]
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POSNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """  Serial Number base data type  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Serial Number format  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Current Prefix setting  """  
      self.Plant:str = obj["Plant"]
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      self.SNMask:str = obj["SNMask"]
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POSelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SNPrefix:str = obj["SNPrefix"]
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask that was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment, needed here to keep POSelectedSerialNumbers in sync with SelectedSerialNumbers  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: needed here to keep POSelctedSerialNumbers in sync with SelectedSerialNumbers  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackOutRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      self.EntryPerson:str = obj["EntryPerson"]
      self.LabelComment:str = obj["LabelComment"]
      self.ShipComment:str = obj["ShipComment"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.CustNum:int = obj["CustNum"]
      self.PackLine:int = obj["PackLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.LineType:str = obj["LineType"]
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      self.JobNum:str = obj["JobNum"]
      self.PartNum:str = obj["PartNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.ShipCmpl:bool = obj["ShipCmpl"]
      self.BinNum:str = obj["BinNum"]
      self.ShpConNum:int = obj["ShpConNum"]
      self.LotNum:str = obj["LotNum"]
      self.DimCode:str = obj["DimCode"]
      self.DUM:str = obj["DUM"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.InvoiceComment:str = obj["InvoiceComment"]
      self.ShipStatus:str = obj["ShipStatus"]
      self.Stage:str = obj["Stage"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      self.BTConNum:int = obj["BTConNum"]
      self.BTCustID:str = obj["BTCustID"]
      self.InvQty:int = obj["InvQty"]
      self.PackQty:int = obj["PackQty"]
      self.ShipAddr:str = obj["ShipAddr"]
      self.StockPart:bool = obj["StockPart"]
      self.CustName:str = obj["CustName"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.KitNumPartDescription:str = obj["KitNumPartDescription"]
      self.KitPartRev:str = obj["KitPartRev"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.TotRelQty:int = obj["TotRelQty"]
      self.PromptPartRev:bool = obj["PromptPartRev"]
      self.PromptKitRevision:bool = obj["PromptKitRevision"]
      self.PromptJobNum:bool = obj["PromptJobNum"]
      self.PromptOrderRel:bool = obj["PromptOrderRel"]
      self.PromptKit:bool = obj["PromptKit"]
      self.AutoQuantity:bool = obj["AutoQuantity"]
      self.PromptOrderLine:bool = obj["PromptOrderLine"]
      self.ToPlant:str = obj["ToPlant"]
      self.FromPlant:str = obj["FromPlant"]
      self.FromAddr:str = obj["FromAddr"]
      self.PackMode:str = obj["PackMode"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.BTCustNum:int = obj["BTCustNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.NumMatchs:int = obj["NumMatchs"]
      self.PackOutNum:int = obj["PackOutNum"]
      """  Unique identifer for the PackOut dataset  """  
      self.Plant:str = obj["Plant"]
      self.IsInvoiced:bool = obj["IsInvoiced"]
      self.MFTransNum:str = obj["MFTransNum"]
      self.TrackingNumber:str = obj["TrackingNumber"]
      self.MFCallTag:str = obj["MFCallTag"]
      self.MFPickUpNum:str = obj["MFPickUpNum"]
      self.MFZone:str = obj["MFZone"]
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      self.MFOversized:bool = obj["MFOversized"]
      self.MFTemplate:str = obj["MFTemplate"]
      self.MFDimWeight:int = obj["MFDimWeight"]
      self.ShipDate:str = obj["ShipDate"]
      self.VendorID:str = obj["VendorID"]
      self.Quantity:int = obj["Quantity"]
      self.TotPackedQty:int = obj["TotPackedQty"]
      self.RemainQty:int = obj["RemainQty"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Set from ShipHead.HasCartonLines  """  
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ShipStatusXlate:str = obj["ShipStatusXlate"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgClass:str = obj["PkgClass"]
      self.KitFlag:str = obj["KitFlag"]
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height of packaging  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  If zero the packaging height prompt is enabled.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length of packaging  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is to be enabled.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width of packaging  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width prompt is enabled.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      self.CODAmount:int = obj["CODAmount"]
      """  COD Amount  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Decared Insurance Amount  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Logical indicating this pack has phantom cases.  Used by UI to disable phantom controlled fields.  """  
      self.Weight:int = obj["Weight"]
      """  Pack weight.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Masterpack PackID this pack is on.  """  
      self.EnableWhseBin:bool = obj["EnableWhseBin"]
      """  Enables the Warehouse and Bin fields on the UIApp  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  0 indicates Pkg Size UOM should be enabled  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      self.JobShipUOM:str = obj["JobShipUOM"]
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Boolean indicating if the package control functionality should be enabled.  """  
      self.PCID:str = obj["PCID"]
      self.ShipToWarning:str = obj["ShipToWarning"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      """  temp message to display newly created legal number  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number associated with pack  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID associated with Pack.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  TranDocType Description associated with this Pack  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.KitAttributeSetDescription:str = obj["KitAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.KitAttributeSetShortDescription:str = obj["KitAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for pack out  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      self.EnableReadyToInvoice:bool = obj["EnableReadyToInvoice"]
      """  Indicates if Ready to Invoice is enabled or not  """  
      self.ShipToInactive:bool = obj["ShipToInactive"]
      """  Indicates if the record is inactive.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackOutTableset:
   def __init__(self, obj):
      self.PackOut:list[Erp_Tablesets_PackOutRow] = obj["PackOut"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.POSelectedSerialNumbers:list[Erp_Tablesets_POSelectedSerialNumbersRow] = obj["POSelectedSerialNumbers"]
      self.POSNFormat:list[Erp_Tablesets_POSNFormatRow] = obj["POSNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.OrigCountry:int = obj["OrigCountry"]
      """  CountryNum for Country of Origin  """  
      self.QtyPerc:int = obj["QtyPerc"]
      """  Qty percent of this part which is from this country of origin.  """  
      self.ValuePerc:int = obj["ValuePerc"]
      """  Value percent of this part from this country of origin.  """  
      self.Primary:bool = obj["Primary"]
      """  Is this the primary country of origin for this part  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFOrdDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.OrderFirm:bool = obj["OrderFirm"]
      """  Indicates an Unfirm Transfer Order.  Similar to JobFirm  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ManualOrder:bool = obj["ManualOrder"]
      """  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job number of the job supplying the parts for this record (FromSite)  """  
      self.DemandJobNum:str = obj["DemandJobNum"]
      """  Job number of the job demand for the parts on this record (ToSite)  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity  """  
      self.AdditionalQty:int = obj["AdditionalQty"]
      """  Additional quantity beyond the initial requirement to be transferred  """  
      self.FirmDate:str = obj["FirmDate"]
      """  Date transfer suggestion went firm  """  
      self.FirmUser:str = obj["FirmUser"]
      """  User who made the transfer suggestion firm  """  
      self.DemandAsmSeq:int = obj["DemandAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.DemandMtlSeq:int = obj["DemandMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SupplyAsmSeq:int = obj["SupplyAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.SupplyMtlSeq:int = obj["SupplyMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.StockTrans:bool = obj["StockTrans"]
      """  Indicates if this requirement/receipt affects stock.  """  
      self.OurStockQtyUOM:str = obj["OurStockQtyUOM"]
      """   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQtyUOM:str = obj["SellingQtyUOM"]
      """   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQty:int = obj["SellingQty"]
      """  Selling Quantity  """  
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      """  Selling Shipped Quantity  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.TransferContractID:str = obj["TransferContractID"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  """  
      self.TransferLinkToContract:bool = obj["TransferLinkToContract"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the transfer order line should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the transfer order line is ready to be fulfilled.  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      self.BinNum:str = obj["BinNum"]
      self.DimCode:str = obj["DimCode"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  DimCodeDimCodeDescription  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockQty * DimConvFactor  """  
      self.DUM:str = obj["DUM"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Transfer Order Detail is allocated against.  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Descriptive Text of OpenLine Field  """  
      self.LotNum:str = obj["LotNum"]
      self.Packages:int = obj["Packages"]
      self.PCID:str = obj["PCID"]
      self.PkgClass:str = obj["PkgClass"]
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      """  PkgClassDescription  """  
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  PkgCodeDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      self.Selected:bool = obj["Selected"]
      self.StagingBinDesc:str = obj["StagingBinDesc"]
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  This order inventory quantity  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.TotNetWeight:int = obj["TotNetWeight"]
      self.Weight:int = obj["Weight"]
      self.CreateOrder:bool = obj["CreateOrder"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this release is in the fulfillment queue.  """  
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PartDescTrackInventoryAttributes:bool = obj["PartDescTrackInventoryAttributes"]
      self.PartDescAttrClassID:str = obj["PartDescAttrClassID"]
      self.PartDescPricePerCode:str = obj["PartDescPricePerCode"]
      self.PartDescTrackSerialNum:bool = obj["PartDescTrackSerialNum"]
      self.PartDescPartDescription:str = obj["PartDescPartDescription"]
      self.PartDescTrackDimension:bool = obj["PartDescTrackDimension"]
      self.PartDescSalesUM:str = obj["PartDescSalesUM"]
      self.PartDescIUM:str = obj["PartDescIUM"]
      self.PartDescSellingFactor:int = obj["PartDescSellingFactor"]
      self.PartDescTrackLots:bool = obj["PartDescTrackLots"]
      self.PartDescTrackInventoryByRevision:bool = obj["PartDescTrackInventoryByRevision"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.StageWhseCodeDescription:str = obj["StageWhseCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFOrdHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains picking  comments about the overall order. These will be printed on the picking lists.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTo information defined for this release should be used.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time ShipTo Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time ShipTo first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time ShipTo second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time ShipTo third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portionof the One Time ShipTo address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or provine portion of the One Time ShipTo address.  """  
      self.OTSZip:str = obj["OTSZip"]
      """  The zip or postal code portion of the One Time ShipTo address.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time ShipTo contact name.  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax Number for the One Time ShipTo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the transfer order is ready to be fulfilled.  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.RequestDate:str = obj["RequestDate"]
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.UpdateDtlRecords:bool = obj["UpdateDtlRecords"]
      """  Flag to indicate if details need to be refreshed after changing the header.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EntryPersonName:str = obj["EntryPersonName"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...).  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is defaulted as Job Number.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.requestdate:str = obj["requestdate"]
      """  requestdate  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Calculated price for the item being transferred.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Transfer Order.  This quantity is in the IUM unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AllocatedShippedQty:int = obj["AllocatedShippedQty"]
      """  If AMM is licensed this column will hold how much of this shipment was allocated prior to the shipment in case this shipment is ever "unshipped"  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      """  Are there available serial numbers?  """  
      self.direct_transfer:bool = obj["direct_transfer"]
      """  direct-transfer  """  
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockShippedQty * DimConvFactor  """  
      self.LineShipped:bool = obj["LineShipped"]
      """  Indicates if the Shipment line has been shipped  """  
      self.OrderShipmentQty:int = obj["OrderShipmentQty"]
      """  Current Shipment in OrderUOM  """  
      self.OrderUOM:str = obj["OrderUOM"]
      """  UOM from Transfer Order  """  
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by the freight web service  """  
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by the freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by the freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by the freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by the freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by the freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by the freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by the freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by the freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by the freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by the freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by the freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by the freight web service  """  
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by the freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by the freight web service  """  
      self.Received:bool = obj["Received"]
      """  Indicates if the Shipment line has been received  """  
      self.RemainingQty:int = obj["RemainingQty"]
      """  The remaining quantity  """  
      self.RequestQty:int = obj["RequestQty"]
      """  The request quantity  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  The shipped quantity  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Ship Status of the Transfer Order Shipment line, copied from the Transfer Order Shipment header.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      """  Enable Attribute Set Search  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
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

class Erp_Tablesets_TFShipHeadInsuranceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PackNum:int = obj["PackNum"]
      """  PackNum  """  
      self.InsuranceSeq:int = obj["InsuranceSeq"]
      """  InsuranceSeq  """  
      self.Type:str = obj["Type"]
      """  Insurance Type  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Insurance Company Name  """  
      self.PolicyNum:str = obj["PolicyNum"]
      """  Insurance Policy Number  """  
      self.Premium:int = obj["Premium"]
      """  Insurance Premium  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.directtransfer:bool = obj["directtransfer"]
      """  directtransfer  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Third address line  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFromAddr:str = obj["DspFromAddr"]
      """  Display for the Ship From Address  """  
      self.DspShipAddr:str = obj["DspShipAddr"]
      """  Display for the Ship To Address  """  
      self.TranStatus:str = obj["TranStatus"]
      """  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.TranStatusDescription:str = obj["TranStatusDescription"]
      """  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      """  Flag to control if the Shipped flag is enabled/disabled  """  
      self.SlipStatus:str = obj["SlipStatus"]
      """  Translated field of ShipStatus  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height prompt is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  1 = disable / 0 = enable  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for subcontract shipments  """  
      self.CalcPSPrices:bool = obj["CalcPSPrices"]
      """  Intended for internal use.  Indicates if prices are to be calculated  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if the transaction document type is available for input  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.PackClssDescription:str = obj["PackClssDescription"]
      """  Full description of the Packaging Classification.  """  
      self.PackingDescription:str = obj["PackingDescription"]
      """  Full description of Packing Code.  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadListTableset:
   def __init__(self, obj):
      self.TFShipHeadList:list[Erp_Tablesets_TFShipHeadListRow] = obj["TFShipHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TFShipHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.directtransfer:bool = obj["directtransfer"]
      """  directtransfer  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Third address line  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGCarrierCUIT:str = obj["AGCarrierCUIT"]
      """  AGCarrierCUIT  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.AGTrackLicense:str = obj["AGTrackLicense"]
      """  AGTrackLicense  """  
      self.AGShippingWay:str = obj["AGShippingWay"]
      """  AGShippingWay  """  
      self.AGCOTMark:bool = obj["AGCOTMark"]
      """  AGCOTMark  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Creation date and time  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Certificate Serial Number  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Certificate  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  Fiscal Folio (UUID)  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  SAT Certificate Serial Number  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Digital Seal  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  SAT Seal  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  Original String  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  TFD Original String  """  
      self.MXSerie:str = obj["MXSerie"]
      """  Serie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  Folio  """  
      self.MXETD:str = obj["MXETD"]
      """  Estimated Date and Time of Departure  """  
      self.MXETA:str = obj["MXETA"]
      """  Estimated Date and Time of Arrival  """  
      self.MXDistance:int = obj["MXDistance"]
      """  Distance in Km  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.MXCartaPorteStatus:str = obj["MXCartaPorteStatus"]
      """  Carta Porte Status  """  
      self.VehicleLicensePlate:str = obj["VehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.VehicleType:str = obj["VehicleType"]
      """  Vehicle Type  """  
      self.VehicleYear:int = obj["VehicleYear"]
      """  Vehicle Year  """  
      self.DriverID:str = obj["DriverID"]
      """  Driver  """  
      self.MXCancelFiscalFolio:str = obj["MXCancelFiscalFolio"]
      """  MXCancelFiscalFolio  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number.  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.DspFromAddr:str = obj["DspFromAddr"]
      """  Display for the Ship From Address  """  
      self.DspShipAddr:str = obj["DspShipAddr"]
      """  Display for the Ship To Address  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      """  Flag to control if the Shipped flag is enabled/disabled  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if the transaction document type is available for input  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for subcontract shipments  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height prompt is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  1 = disable / 0 = enable  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width is enabled.  """  
      self.SlipStatus:str = obj["SlipStatus"]
      """  Translated field of ShipStatus  """  
      self.TranStatus:str = obj["TranStatus"]
      """  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.TranStatusDescription:str = obj["TranStatusDescription"]
      """  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  """  
      self.VNAccordingToDemand:str = obj["VNAccordingToDemand"]
      self.VNCarrier:str = obj["VNCarrier"]
      self.VNContractNumber:str = obj["VNContractNumber"]
      self.VNDate:str = obj["VNDate"]
      self.VNFor:str = obj["VNFor"]
      self.VNFrom:str = obj["VNFrom"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.CalcPSPrices:bool = obj["CalcPSPrices"]
      """  Intended for internal use.  Indicates if prices are to be calculated  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Logical indicating if the package control functionality should be enabled.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer order number  """  
      self.MXETADate:str = obj["MXETADate"]
      """  Estimated Date of Arrival  """  
      self.MXETATime:int = obj["MXETATime"]
      """  Estimated Time of Arrival  """  
      self.MXETDDate:str = obj["MXETDDate"]
      """  Estimated Date of Departure  """  
      self.MXETDTime:int = obj["MXETDTime"]
      """  Estimated Time of Departure  """  
      self.EnablePhantom:bool = obj["EnablePhantom"]
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      self.MXVehicleWeight:int = obj["MXVehicleWeight"]
      """  Vehicle Weight (in tons)  """  
      self.MXIdCCP:str = obj["MXIdCCP"]
      """  A unique Carta Porte identification number assigned by Epicor  """  
      self.MXCustomsRegime:str = obj["MXCustomsRegime"]
      """  Customs Regime for Export transaction.  """  
      self.MXReverseLogistics:bool = obj["MXReverseLogistics"]
      """  Check box to specify the use of reverse logistic, collection or devolution services when shipping goods.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.AGLegalNumCnfgDescription:str = obj["AGLegalNumCnfgDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.PackClssDescription:str = obj["PackClssDescription"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadTrailerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing Slip  """  
      self.LicensePlate:str = obj["LicensePlate"]
      """  License Plate for Trailer  """  
      self.Type:str = obj["Type"]
      """  Type of Trailer  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipUPSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email Address  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Notify Email address when shipped  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating if the UPS Quantum View fields are to be enabled  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TranDirectOrderTableset:
   def __init__(self, obj):
      self.TFOrdHed:list[Erp_Tablesets_TFOrdHedRow] = obj["TFOrdHed"]
      self.TFOrdDtl:list[Erp_Tablesets_TFOrdDtlRow] = obj["TFOrdDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TransOrderShipTableset:
   def __init__(self, obj):
      self.TFShipHead:list[Erp_Tablesets_TFShipHeadRow] = obj["TFShipHead"]
      self.TFShipHeadAttch:list[Erp_Tablesets_TFShipHeadAttchRow] = obj["TFShipHeadAttch"]
      self.TFShipDtl:list[Erp_Tablesets_TFShipDtlRow] = obj["TFShipDtl"]
      self.ShipCOO:list[Erp_Tablesets_ShipCOORow] = obj["ShipCOO"]
      self.CartonTrkDtl:list[Erp_Tablesets_CartonTrkDtlRow] = obj["CartonTrkDtl"]
      self.TFShipHeadInsurance:list[Erp_Tablesets_TFShipHeadInsuranceRow] = obj["TFShipHeadInsurance"]
      self.TFShipHeadTrailer:list[Erp_Tablesets_TFShipHeadTrailerRow] = obj["TFShipHeadTrailer"]
      self.TFShipUPS:list[Erp_Tablesets_TFShipUPSRow] = obj["TFShipUPS"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTransOrderShipTableset:
   def __init__(self, obj):
      self.TFShipHead:list[Erp_Tablesets_TFShipHeadRow] = obj["TFShipHead"]
      self.TFShipHeadAttch:list[Erp_Tablesets_TFShipHeadAttchRow] = obj["TFShipHeadAttch"]
      self.TFShipDtl:list[Erp_Tablesets_TFShipDtlRow] = obj["TFShipDtl"]
      self.ShipCOO:list[Erp_Tablesets_ShipCOORow] = obj["ShipCOO"]
      self.CartonTrkDtl:list[Erp_Tablesets_CartonTrkDtlRow] = obj["CartonTrkDtl"]
      self.TFShipHeadInsurance:list[Erp_Tablesets_TFShipHeadInsuranceRow] = obj["TFShipHeadInsurance"]
      self.TFShipHeadTrailer:list[Erp_Tablesets_TFShipHeadTrailerRow] = obj["TFShipHeadTrailer"]
      self.TFShipUPS:list[Erp_Tablesets_TFShipUPSRow] = obj["TFShipUPS"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExpireDate_input:
   """ Required : 
   ExpirationDate
   EffectiveDAte
   Duration
   modifier
   """  
   def __init__(self, obj):
      self.ExpirationDate:str = obj["ExpirationDate"]
      self.EffectiveDAte:str = obj["EffectiveDAte"]
      self.Duration:int = obj["Duration"]
      self.modifier:str = obj["modifier"]
      pass

class ExpireDate_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GenerateDigitalSignature_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GenerateDigitalSignature_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
      pass

class GetCartonPackaging_input:
   """ Required : 
   ipPkgCode
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      pass

class GetCartonPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPkgHeight:int = obj["parameters"]
      self.opPkgWidth:int = obj["parameters"]
      self.opPkgLength:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name  """  
      self.fieldName:str = obj["fieldName"]
      """  Field Name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDirectOrderDS_input:
   """ Required : 
   tfOrdNum
   ds
   """  
   def __init__(self, obj):
      self.tfOrdNum:str = obj["tfOrdNum"]
      """  Unique Identifier for the Transfer Order  """  
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class GetDirectOrderDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDirectShipDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class GetDirectShipDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDisablePackOut_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class GetEnablePackageControl_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  bool  """  
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.opPromptForNum:bool = obj["opPromptForNum"]
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
      self.returnObj:list[Erp_Tablesets_TFShipHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCartonTrkDtl_input:
   """ Required : 
   ds
   shipmentType
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.shipmentType:str = obj["shipmentType"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewCartonTrkDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDirectOrderLine_input:
   """ Required : 
   TFOrdNum
   NeedByDate
   RequestDate
   ds
   """  
   def __init__(self, obj):
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order Number  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Ship Date  """  
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class GetNewDirectOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDirectOrder_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class GetNewDirectOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFromOrderWithPCID_input:
   """ Required : 
   ordNum
   checkPCID
   ds
   """  
   def __init__(self, obj):
      self.ordNum:str = obj["ordNum"]
      """  The transfer order number  """  
      self.checkPCID:bool = obj["checkPCID"]
      """  When true, prevent orders that have allocations with PCID, from being created.  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetNewFromOrderWithPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFromOrder_input:
   """ Required : 
   ordNum
   ds
   """  
   def __init__(self, obj):
      self.ordNum:str = obj["ordNum"]
      """  The transfer order number  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetNewFromOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipCOO_input:
   """ Required : 
   ds
   relatedToFile
   packNum
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      pass

class GetNewShipCOO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFShipDtl_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewTFShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFShipHeadAttch_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewTFShipHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFShipHeadInsurance_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewTFShipHeadInsurance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFShipHeadTrailer_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewTFShipHeadTrailer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFShipHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetNewTFShipHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFShipUPS_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewTFShipUPS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOPackClass_input:
   """ Required : 
   ipPkgClass
   ds
   """  
   def __init__(self, obj):
      self.ipPkgClass:str = obj["ipPkgClass"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class GetPOPackClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOPackaging_input:
   """ Required : 
   ipPkgCode
   ds
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class GetPOPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackClass_input:
   """ Required : 
   ipPkgClass
   ds
   """  
   def __init__(self, obj):
      self.ipPkgClass:str = obj["ipPkgClass"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetPackClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackaging_input:
   """ Required : 
   ipPkgCode
   ds
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPayBTFlagDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetPayBTFlagDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTFShipHead
   whereClauseTFShipHeadAttch
   whereClauseTFShipDtl
   whereClauseShipCOO
   whereClauseCartonTrkDtl
   whereClauseTFShipHeadInsurance
   whereClauseTFShipHeadTrailer
   whereClauseTFShipUPS
   whereClauseLegalNumGenOpts
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTFShipHead:str = obj["whereClauseTFShipHead"]
      self.whereClauseTFShipHeadAttch:str = obj["whereClauseTFShipHeadAttch"]
      self.whereClauseTFShipDtl:str = obj["whereClauseTFShipDtl"]
      self.whereClauseShipCOO:str = obj["whereClauseShipCOO"]
      self.whereClauseCartonTrkDtl:str = obj["whereClauseCartonTrkDtl"]
      self.whereClauseTFShipHeadInsurance:str = obj["whereClauseTFShipHeadInsurance"]
      self.whereClauseTFShipHeadTrailer:str = obj["whereClauseTFShipHeadTrailer"]
      self.whereClauseTFShipUPS:str = obj["whereClauseTFShipUPS"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetScale_input:
   """ Required : 
   workstationID
   """  
   def __init__(self, obj):
      self.workstationID:str = obj["workstationID"]
      """  Workstation ID  """  
      pass

class GetScale_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ScaleID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ipPartNum
   attributeSetID
   ipWarehouseCode
   ipBinNum
   ipQuantity
   ipUOM
   ipTransType
   ipSourceRowID
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part Number  """  
      self.attributeSetID:int = obj["attributeSetID"]
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code  """  
      self.ipBinNum:str = obj["ipBinNum"]
      """  Bin Num  """  
      self.ipQuantity:int = obj["ipQuantity"]
      """  Quantity  """  
      self.ipUOM:str = obj["ipUOM"]
      """  UOM  """  
      self.ipTransType:str = obj["ipTransType"]
      """  TransType  """  
      self.ipSourceRowID:str = obj["ipSourceRowID"]
      """  sourceRowID  """  
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetShipCOOTotals_input:
   """ Required : 
   iPackNum
   iPackLine
   ds
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  Pack Number  """  
      self.iPackLine:int = obj["iPackLine"]
      """  Pack Line Number  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetShipCOOTotals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalQuantityPercent:int = obj["parameters"]
      self.totalValuePercent:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetTranDocTypeID_input:
   """ Required : 
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  TranDocTypeID supplied  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class GetTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
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

class IsSerialTracked_input:
   """ Required : 
   ipPart
   ipWhse
   """  
   def __init__(self, obj):
      self.ipPart:str = obj["ipPart"]
      """  Part  """  
      self.ipWhse:str = obj["ipWhse"]
      pass

class IsSerialTracked_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangeShipViaCode_input:
   """ Required : 
   shipViaCode
   ds
   """  
   def __init__(self, obj):
      self.shipViaCode:str = obj["shipViaCode"]
      """  New ShipVia Code  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class OnChangeShipViaCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingTFOrdDtlAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class OnChangingTFOrdDtlAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingTFOrdDtlNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class OnChangingTFOrdDtlNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingTFShipDtlAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class OnChangingTFShipDtlAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingTFShipDtlNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class OnChangingTFShipDtlNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POChangeStatus_input:
   """ Required : 
   ipStatus
   ds
   """  
   def __init__(self, obj):
      self.ipStatus:str = obj["ipStatus"]
      """  Selected Status
            Valid Options: Open, Close, Void, UnVoid, Freight, UnFreight, Stage  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POChangeStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POCreateDtlList_input:
   """ Required : 
   ipOrderNum
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipOrderNum:str = obj["ipOrderNum"]
      """  TFOrdNum value  """  
      self.ipPackNum:int = obj["ipPackNum"]
      """  PackNum value  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POCreateDtlList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POFindBuffer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POFindBuffer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.Found:int = obj["parameters"]
      self.Rowident:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POGetDtlList_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Carton to get the detail lines from  """  
      pass

class POGetDtlList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
      pass

class POGetNewWithDtl_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class POGetNewWithDtl_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
      pass

class POGetNew_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing number  """  
      pass

class POGetNew_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
      pass

class POUndo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POUndo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POUpdateHeader_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POUpdateHeader_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class POUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPackNum:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreDeleteDirectShip_input:
   """ Required : 
   PackNum
   PackLine
   """  
   def __init__(self, obj):
      self.PackNum:int = obj["PackNum"]
      """  Pack number.  """  
      self.PackLine:int = obj["PackLine"]
      """  Pack line number.  """  
      pass

class PreDeleteDirectShip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreDeselectSN_input:
   """ Required : 
   ipPackNum
   ipPackLine
   ipPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipPackLine:int = obj["ipPackLine"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class PreDeselectSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreShipPack_input:
   """ Required : 
   ipTFShipHeadRowID
   """  
   def __init__(self, obj):
      self.ipTFShipHeadRowID:str = obj["ipTFShipHeadRowID"]
      """  TFShipHead.SysRowID  """  
      pass

class PreShipPack_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cErrorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreUnShipPack_input:
   """ Required : 
   proposedShipped
   ipTFShipHeadRowID
   """  
   def __init__(self, obj):
      self.proposedShipped:bool = obj["proposedShipped"]
      """  Proposed value from UI  """  
      self.ipTFShipHeadRowID:str = obj["ipTFShipHeadRowID"]
      """  TFShipHead.SysRowID  """  
      pass

class PreUnShipPack_output:
   def __init__(self, obj):
      pass

class RemovePCID_input:
   """ Required : 
   ipPackNum
   ipPCID
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  ipPackNum  """  
      self.ipPCID:str = obj["ipPCID"]
      """  ipPCID  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class RemovePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.opPCIDCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class SetUPSQVEnable_input:
   """ Required : 
   ipQVEnable
   ds
   """  
   def __init__(self, obj):
      self.ipQVEnable:bool = obj["ipQVEnable"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class SetUPSQVEnable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetUPSQVShipStatus_input:
   """ Required : 
   ipShipStatus
   ds
   """  
   def __init__(self, obj):
      self.ipShipStatus:str = obj["ipShipStatus"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class SetUPSQVShipStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ShipPackingSlip_input:
   """ Required : 
   ipTFShipHeadRowid
   ipReturn
   """  
   def __init__(self, obj):
      self.ipTFShipHeadRowid:str = obj["ipTFShipHeadRowid"]
      """  The rowid of the TFShipHead to ship  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      pass

class ShipPackingSlip_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
      pass

class TFOrdDtl_OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

class TFOrdDtl_OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TranDirectOrderTableset] = obj["ds"]
      pass

      """  output parameters  """  

class TFShipDtl_OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class TFShipDtl_OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UnShipPackingSlip_input:
   """ Required : 
   ipTFShipHeadRowid
   ipReturn
   """  
   def __init__(self, obj):
      self.ipTFShipHeadRowid:str = obj["ipTFShipHeadRowid"]
      """  The rowid of the TFShipHead to unship  """  
      self.ipReturn:bool = obj["ipReturn"]
      """  Logical used to determine if you would like the dataset refreshed and brought back.  """  
      pass

class UnShipPackingSlip_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTransOrderShipTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTransOrderShipTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePackCODWithCarton_input:
   """ Required : 
   ipPackNum
   ipCaseNum
   ipOldCOD
   ipCOD
   ipFlag
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipCaseNum:int = obj["ipCaseNum"]
      self.ipOldCOD:int = obj["ipOldCOD"]
      self.ipCOD:int = obj["ipCOD"]
      self.ipFlag:bool = obj["ipFlag"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class UpdatePackCODWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePackDeclaredWithCarton_input:
   """ Required : 
   ipPackNum
   ipCaseNum
   ipOldDeclared
   ipDeclared
   ipDeclaredFlag
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipCaseNum:int = obj["ipCaseNum"]
      self.ipOldDeclared:int = obj["ipOldDeclared"]
      self.ipDeclared:int = obj["ipDeclared"]
      self.ipDeclaredFlag:bool = obj["ipDeclaredFlag"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class UpdatePackDeclaredWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePackWeightWithCarton_input:
   """ Required : 
   ipPackNum
   ipOldWeight
   ipWeight
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipOldWeight:int = obj["ipOldWeight"]
      self.ipWeight:int = obj["ipWeight"]
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class UpdatePackWeightWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBinCode_input:
   """ Required : 
   ipWhse
   ipBinNum
   """  
   def __init__(self, obj):
      self.ipWhse:str = obj["ipWhse"]
      self.ipBinNum:str = obj["ipBinNum"]
      pass

class ValidateBinCode_output:
   def __init__(self, obj):
      pass

class ValidatePartNum_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class ValidatePartNum_output:
   def __init__(self, obj):
      pass

class ValidateSN_input:
   """ Required : 
   ipWarehouseCode
   ipPartNum
   attributeSetID
   ipTFOrdNum
   ipTFOrdLine
   serialNumber
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  The Warhouse Code  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number  """  
      self.attributeSetID:int = obj["attributeSetID"]
      self.ipTFOrdNum:str = obj["ipTFOrdNum"]
      """  The Transfer Order Number  """  
      self.ipTFOrdLine:int = obj["ipTFOrdLine"]
      """  The Transfer Order Line  """  
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   ipPackNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Reason for the void  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderShipTableset] = obj["returnObj"]
      pass

class WarnNegativeBinOH_input:
   """ Required : 
   ipBinNum
   ds
   """  
   def __init__(self, obj):
      self.ipBinNum:str = obj["ipBinNum"]
      """  The new proposed TFShipDtl.BinNum value  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class WarnNegativeBinOH_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      self.outNegQtyAction:str = obj["parameters"]
      pass

      """  output parameters  """  

class WarnNegativeBinQty_input:
   """ Required : 
   ipDisplayQty
   ds
   """  
   def __init__(self, obj):
      self.ipDisplayQty:int = obj["ipDisplayQty"]
      """  The new proposed TFShipDtl.DisplayShipQty value  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class WarnNegativeBinQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      self.outNegQtyAction:str = obj["parameters"]
      pass

      """  output parameters  """  

class WarnNegativeLotOH_input:
   """ Required : 
   packNum
   packLine
   ipLotNum
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Pack Number to be modified  """  
      self.packLine:int = obj["packLine"]
      """  Pack Line to be modified  """  
      self.ipLotNum:str = obj["ipLotNum"]
      """  The new proposed TFShipDtl.LotNum value  """  
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      pass

class WarnNegativeLotOH_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderShipTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      self.outNegQtyAction:str = obj["parameters"]
      pass

      """  output parameters  """  

